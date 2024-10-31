from django import forms
from .models import SocialMediaPost

class SocialMediaPostForm(forms.ModelForm):
    class Meta:
        model = SocialMediaPost
        fields = ['platform', 'content', 'scheduled_time']
