from rest_framework import serializers
from pokemon.models import Pokemon

# pokemon serializer
class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'