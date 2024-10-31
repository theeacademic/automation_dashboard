# automated_testing/forms.py
from django import forms

class AutomatedTestingForm(forms.Form):
    test_name = forms.CharField(max_length=100)
    test_description = forms.CharField(widget=forms.Textarea)
    # Add any other fields as necessary
