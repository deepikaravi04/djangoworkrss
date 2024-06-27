from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.apps import apps  # Add this import

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'upworkrss.settings')

app = Celery('upworkrss')

app.config_from_object('django.conf:settings', namespace='CELERY')

# This line will automatically discover tasks from all installed apps
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])


@app.task
def hello_task():
    print("Heello from function")
    return "HEllo"


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
