from channel.models import channel
from .serializer import channelSerializer
from rest_framework import viewsets, permissions

# Pokemon Viewset

class channelViewSet(viewsets.ModelViewSet):
    queryset = channel.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = channelSerializer
