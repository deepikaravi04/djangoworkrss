from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_feeder, name='home_feeder'),
    path('display_jobs/', views.display_jobs, name='display_jobs'),
    path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),
    path('add_rss_feed_link/', views.add_rss_feed_link, name='add_rss_feed_link'),
    path('view_rss_feed_links/', views.view_rss_feed_links, name='view_rss_feed_links'),
    path('delete_rss_feed_link/<int:link_id>/', views.delete_rss_feed_link, name='delete_rss_feed_link'),
    path('add_job_filter_term/', views.add_job_filter_term, name='add_job_filter_term'),
    path('view_job_filter_terms/', views.view_job_filter_terms, name='view_job_filter_terms'),
    path('delete_job_filter_term/<int:filter_id>/', views.delete_job_filter_term, name='delete_job_filter_term'),
]
