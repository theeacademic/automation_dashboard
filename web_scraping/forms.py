# web_scraping/forms.py
from django import forms
from .models import WebScrapingTask  # Make sure this model exists

class WebScrapingTaskForm(forms.ModelForm):
    class Meta:
        model = WebScrapingTask
        fields = ['url', 'frequency']  # Adjust fields as necessary
