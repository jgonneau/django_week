from rest_framework import serializers
from message.models import message

# pokemon serializer
class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = '__all__'
