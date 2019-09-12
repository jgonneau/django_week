from userMessage.models import userMessage
from .serializer import userMessageSerializer
from rest_framework import viewsets, permissions

# Pokemon Viewset

class userMessageViewSet(viewsets.ModelViewSet):
    queryset = userMessage.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = userMessageSerializer
