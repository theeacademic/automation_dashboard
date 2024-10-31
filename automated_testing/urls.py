from django.urls import path
from . import views

app_name = 'automated_testing'  # This sets the namespace

urlpatterns = [
    path('add/', views.add_test, name='add_test'),
    # Add other URL patterns for this app here
]
