from rest_framework import serializers
from channel.models import channel

# pokemon serializer
class channelSerializer(serializers.ModelSerializer):
    class Meta:
        model = channel
        fields = '__all__'
