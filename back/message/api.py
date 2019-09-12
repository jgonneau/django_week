from message.models import message
from .serializer import messageSerializer
from rest_framework import viewsets, permissions

# Pokemon Viewset

class messageViewSet(viewsets.ModelViewSet):
    queryset = message.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = messageSerializer
