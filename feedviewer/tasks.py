from celery import shared_task
from .models import RSSFeedLink, JobFilterTerm, JobListing
import feedparser
from dateutil import parser as date_parser
from telegram import Bot
from asgiref.sync import sync_to_async
import asyncio
import bleach
import time 

@shared_task
def rss_feed_background_task():

    async def send_message_async(bot_token, group_chat_id, message):
        bot = Bot(token=bot_token)
        max_message_length = 4096  # Telegram message length limit
        if len(message) > max_message_length:
            message = message[:max_message_length]  # Truncate the message if too long
        await bot.send_message(chat_id=group_chat_id, text=message, parse_mode='html')

    async def fetch_rss_feed_links():
        return await sync_to_async(list)(RSSFeedLink.objects.all())

    async def fetch_filter_terms():
        return await sync_to_async(list)(JobFilterTerm.objects.all())

    async def check_job_exists(title):
        return await sync_to_async(JobListing.objects.filter(job_title=title).exists)()

    async def create_job_listing(**kwargs):
        return await sync_to_async(JobListing.objects.create)(**kwargs)

    async def main():
        rssLinks = await fetch_rss_feed_links()
        filter_terms = await fetch_filter_terms()
        filter_term_list = [term.filter_term for term in filter_terms]

        bot_token = '7162513284:AAGUXwYIhA19hFyj8dGV26Qh-TnSJci6soI'
        group_chat_id = '-1002131270840'

        allowed_tags = ['b', 'strong', 'i', 'em', 'u', 'ins', 's', 'strike', 'del', 'code', 'pre', 'a']

        for link in rssLinks:
            feed_url = link.search_link
            feed = feedparser.parse(feed_url)
            if feed.bozo == 0:
                for entry in feed.entries:
                    title = entry.title
                    summary_html = entry.summary
                    published_date = date_parser.parse(entry.published)

                    # Sanitize the summary HTML to only include allowed tags
                    sanitized_summary = bleach.clean(summary_html, tags=allowed_tags, strip=True)

                    # Check if any filter terms are present in title or sanitized summary
                    filter_term_present = any(term.lower() in title.lower() or term.lower() in sanitized_summary.lower() for term in filter_term_list)

                    # Check if job_title already exists
                    job_exists = await check_job_exists(title)

                    if filter_term_present and not job_exists:
                        # Assuming job_search_term and job_price_type are derived from somewhere
                        job_search_term = link.search_term
                        job_price_type = "some_price_type"

                        # Create and save JobListing instance
                        await create_job_listing(
                            job_title=title,
                            job_summary=sanitized_summary,
                            job_published=published_date,
                            job_search_term=job_search_term,
                            job_price_type=job_price_type
                        )

                        # Prepare and send Telegram message
                        message = f"New Job Listing: <b>{title}</b>\nPublished on: {published_date}\n\n{sanitized_summary}"
                        await send_message_async(bot_token, group_chat_id, message)
                        
                        

    # Run the main function in an event loop
    asyncio.run(main())
