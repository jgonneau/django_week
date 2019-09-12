from django.urls import path, include
from rest_framework import routers
from .api import userMessageViewSet

router = routers.DefaultRouter()
router.register('api/userMessage', userMessageViewSet, 'userMessage')

urlpatterns = router.urls
