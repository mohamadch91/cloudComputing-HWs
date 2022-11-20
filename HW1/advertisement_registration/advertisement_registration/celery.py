import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advertisement_registration.settings')
# Create the celery app
app = Celery('advertisement_registration')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()