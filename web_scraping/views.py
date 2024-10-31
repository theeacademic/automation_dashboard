# web_scraping/views.py
from django.shortcuts import render
from .forms import WebScrapingTaskForm  # Ensure this form is defined
from .models import WebScrapingTask     # Ensure this model is defined

def add_task(request):
    if request.method == "POST":
        form = WebScrapingTaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new scraping task to the database
            # Optionally, redirect or add a success message here
    else:
        form = WebScrapingTaskForm()

    # Fetch existing tasks to display
    scraping_tasks = WebScrapingTask.objects.all()
    
    context = {
        'web_scraping_form': form,
        'scraping_tasks': scraping_tasks,
        # Include any other forms or data you want to pass for the dashboard
    }
    return render(request, 'dashboard.html', context)
