from django.contrib import admin
from .models import Profile
from django_private_chat.models import Dialog, Message





admin.site.register(Profile)
#admin.site.register(Message)