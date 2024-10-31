from django.db import models

class SocialMediaPost(models.Model):
    platform = models.CharField(max_length=50)  # e.g., Twitter, Instagram
    content = models.TextField()
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=50, default="Scheduled")

    def __str__(self):
        return f"{self.platform} - {self.content[:30]}..."
