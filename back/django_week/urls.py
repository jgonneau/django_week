from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('message.urls')),
    path('', include('channel.urls')),
    path('', include('userMessage.urls')),
]
