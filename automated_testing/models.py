# automated_testing/models.py
from django.db import models

class AutomatedTest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add other fields as necessary
