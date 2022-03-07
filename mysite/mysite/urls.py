from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('api.urls')),
    path('plans/',include('plans.urls')),
    path('users/',include('users.urls')),
    path('posts/',include('posts.urls')),
    path('hashtag/',include('hashtag.urls')),
    path('questions/',include('questions.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)