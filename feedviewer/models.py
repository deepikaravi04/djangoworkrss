from django.db import models

class RSSFeedLink(models.Model):
    search_link = models.TextField()
    search_term = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return f'{self.search_link} - {self.search_term}'

class JobFilterTerm(models.Model):
    filter_term = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.filter_term

class JobListing(models.Model):
    job_title = models.TextField()
    job_summary = models.TextField()
    job_published = models.DateTimeField()
    job_search_term = models.CharField(max_length=5000)
    job_price_type = models.CharField(max_length=5000)

    def __str__(self):
        return self.job_title
