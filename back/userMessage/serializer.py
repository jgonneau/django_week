from rest_framework import serializers
from userMessage.models import userMessage

# pokemon serializer
class userMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = userMessage
        fields = '__all__'
