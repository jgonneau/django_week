from django.db import models
from rest_framework import routers, serializers, viewsets

class MessageModel(models.Model):
    class Meta:
        app_label = 'message'
    content = models.CharField()
    idUser = models.TextField()
    idChannel = models.TextField()

class MessageSerializer(serializers.Serializer):
    class Meta:
        model = MessageModel
        fields = ['content', 'idUser', 'idChannel']

class MessageViewSet(viewsets.ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer
