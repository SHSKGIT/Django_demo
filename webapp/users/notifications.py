from django.db.models.signals import post_save
from notifications.signals import notify
from .models import User

def my_handler(sender, instance, created, **kwargs):
    notify.send(instance, verb='was saved')