from django import forms
from .models import RSSFeedLink, JobFilterTerm

class RSSFeedLinkForm(forms.ModelForm):
    class Meta:
        model = RSSFeedLink
        fields = ['search_link', 'search_term']

class JobFilterTermForm(forms.ModelForm):
    class Meta:
        model = JobFilterTerm
        fields = ['filter_term']
