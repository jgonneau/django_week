from django.urls import path, include
from rest_framework import routers
from .api import channelViewSet

router = routers.DefaultRouter()
router.register('api/channel', channelViewSet, 'channel')

urlpatterns = router.urls
