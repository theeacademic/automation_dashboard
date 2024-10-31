import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SocialMediaPost  # Assuming you have a model for social media posts
from automated_testing.models import AutomatedTest  # Adjust based on your models
from .forms import SocialMediaPostForm  # Assuming you have a form for creating posts

logger = logging.getLogger(__name__)

def dashboard(request):
    """Render the dashboard page."""
    return render(request, 'dashboard.html')  # Ensure this file exists in your templates folder

def create_post(request):
    """Create a new social media post."""
    if request.method == 'POST':
        form = SocialMediaPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard or wherever appropriate
    else:
        form = SocialMediaPostForm()
    
    return render(request, 'create_post.html', {'form': form})  # Create this template as needed

def view_posts(request):
    """View all social media posts."""
    posts = SocialMediaPost.objects.all()  # Adjust according to your model
    return render(request, 'view_posts.html', {'posts': posts})  # Ensure this template exists

def delete_post(request, post_id):
    """Delete a specific social media post."""
    try:
        post = SocialMediaPost.objects.get(id=post_id)
        post.delete()
        return redirect('view_posts')  # Redirect to the view posts page after deletion
    except SocialMediaPost.DoesNotExist:
        return HttpResponse("Post does not exist.")  # Handle case where post doesn't exist

# views.py
def schedule_post(request):
    if request.method == "POST":
        post_content = request.POST.get('post_content')
        schedule_time = request.POST.get('schedule_time')

        # Here you would save the post to the database

        return redirect('schedule_post')  # Adjust according to your redirect

    # For GET requests, retrieve scheduled posts from the database
    scheduled_posts = []  # Replace with your logic to fetch scheduled posts

    return render(request, 'schedule_post.html', {'scheduled_posts': scheduled_posts})
