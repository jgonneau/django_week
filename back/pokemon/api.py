from pokemon.models import Pokemon 
from .serializer import PokemonSerializer
from rest_framework import viewsets, permissions

# Pokemon Viewset

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PokemonSerializer