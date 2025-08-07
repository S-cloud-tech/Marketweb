import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puddle.settings')
app = Celery('puddle')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
