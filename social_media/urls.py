# social_media/urls.py
from django.urls import path
from .views import schedule_post, dashboard

app_name = 'social_media'  # This sets the namespace

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('schedule/', schedule_post, name='schedule_post'),
    path('schedule/', schedule_post, name='schedule'),
]
