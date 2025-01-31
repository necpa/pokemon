from rest_framework import viewsets
from .models import PokemonSpecies, Pokemon
from .serializers import PokemonSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()  # Tu veux récupérer les espèces de Pokémon
    serializer_class = PokemonSerializer

    def perform_create(self, serializer):
        # Ce code crée l'objet Pokemon lié en fonction des données de la requête
        species = serializer.validated_data.pop('species', None)
        pokemon = Pokemon.objects.create(species=species, **serializer.validated_data)
        pokemon.save()
