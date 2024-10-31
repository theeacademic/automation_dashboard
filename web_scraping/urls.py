# web_scraping/urls.py
from django.urls import path
from . import views

app_name = 'web_scraping'  # This defines the namespace for this app

urlpatterns = [
    path('add_task/', views.add_task, name='add_task'),
    # Add other URL patterns here
]
