# automated_testing/views.py
from django.shortcuts import render
from .forms import AutomatedTestingForm  # Adjust import based on your form's location

def add_test(request):
    if request.method == 'POST':
        form = AutomatedTestingForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()  # or whatever you need to do with the data
            # Redirect or render a success message
    else:
        form = AutomatedTestingForm()
    return render(request, 'add_test.html', {'form': form})
