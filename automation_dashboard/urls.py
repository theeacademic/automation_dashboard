from django.urls import path, include
from django.contrib import admin
from django.urls import path
from social_media import views as social_media_views
from web_scraping import views as web_scraping_views
from automated_testing import views as automated_testing_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('social-media/schedule/', social_media_views.schedule_post, name='schedule_post'),
    path('web-scraping/add-task/', web_scraping_views.add_task, name='add_task'),
    path('automated-testing/add-test/', automated_testing_views.add_test, name='add_test'),
    path('', social_media_views.dashboard, name='dashboard'),  # Main dashboard view
    path('social_media/', include('social_media.urls', namespace='social_media')),  # Add namespace here
    path('web_scraping/', include('web_scraping.urls', namespace='web_scraping')),
    path('automated_testing/', include('automated_testing.urls', namespace='automated_testing')),
]
