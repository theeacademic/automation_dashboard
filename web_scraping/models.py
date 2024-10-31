# web_scraping/models.py
from django.db import models

class WebScrapingTask(models.Model):
    url = models.URLField()
    frequency = models.CharField(max_length=50)  # Adjust the fields as necessary
    # Add other fields as needed

    def __str__(self):
        return self.url
