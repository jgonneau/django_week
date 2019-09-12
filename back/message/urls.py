from django.urls import path, include
from rest_framework import routers
from .api import messageViewSet

router = routers.DefaultRouter()
router.register('api/message', messageViewSet, 'message')

urlpatterns = router.urls
