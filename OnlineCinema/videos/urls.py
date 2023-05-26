from django.contrib import admin
from django.urls import path, include
from .views import index, video_info
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='main'),
    path('video/<int:pk>/', video_info, name='video_info'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)