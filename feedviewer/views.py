from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import RSSFeedLink, JobFilterTerm, JobListing
from .forms import RSSFeedLinkForm, JobFilterTermForm
from datetime import datetime

def home_feeder(request):
    return render(request, "home_feeder.html")

def display_jobs(request):
    jobs = JobListing.objects.order_by('-job_published')
    return render(request, 'display_jobs.html', {'jobs': jobs})

def delete_job(request, job_id):
    job = get_object_or_404(JobListing, id=job_id)
    job.delete()
    messages.success(request, 'Job deleted successfully!')
    return redirect('display_jobs')

def add_rss_feed_link(request):
    if request.method == 'POST':
        form = RSSFeedLinkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Link added successfully!')
            return redirect('add_rss_feed_link')
    else:
        form = RSSFeedLinkForm()
    return render(request, 'add_rss_feed_link.html', {'form': form})

def view_rss_feed_links(request):
    links = RSSFeedLink.objects.all()
    return render(request, 'view_rss_feed_links.html', {'links': links})

def delete_rss_feed_link(request, link_id):
    link = get_object_or_404(RSSFeedLink, id=link_id)
    link.delete()
    messages.success(request, 'RSS feed link deleted successfully!')
    return redirect('view_rss_feed_links')

def add_job_filter_term(request):
    if request.method == 'POST':
        form = JobFilterTermForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filter term added successfully!')
            return redirect('add_job_filter_term')
    else:
        form = JobFilterTermForm()
    return render(request, 'add_job_filter_term.html', {'form': form})

def view_job_filter_terms(request):
    filters = JobFilterTerm.objects.all()
    return render(request, 'view_job_filter_terms.html', {'filters': filters})

def delete_job_filter_term(request, filter_id):
    filter_term = get_object_or_404(JobFilterTerm, id=filter_id)
    filter_term.delete()
    messages.success(request, 'Filter term deleted successfully!')
    return redirect('view_job_filter_terms')
