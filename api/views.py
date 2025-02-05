from rest_framework import viewsets
from .models import Pokemon
from .serializers import PokemonSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()  # Tu veux récupérer les espèces de Pokémon
    serializer_class = PokemonSerializer
