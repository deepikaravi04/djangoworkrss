from django.contrib import admin
from .models import RSSFeedLink, JobFilterTerm, JobListing
# Register your models here.
admin.site.register(RSSFeedLink)
admin.site.register(JobFilterTerm)
admin.site.register(JobListing)