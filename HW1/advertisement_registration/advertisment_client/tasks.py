import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def second_service_taska(id):
    print("second_service_taska")
    user = User.objects.get(pk=id)
    user.username = get_random_string(length=10, allowed_chars=string.ascii_letters)
    user.save()
    