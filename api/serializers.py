from rest_framework import serializers
from .models import Pokemon, PokemonSpecies, PokemonColor, PokemonShape, Type

class PokemonSerializer(serializers.ModelSerializer):
    # Read-only fields for related models
    color = serializers.CharField(source='species.color.identifier', read_only=True)
    shape_id = serializers.CharField(source='species.shape.identifier', read_only=True)
    generation_id = serializers.IntegerField(source='species.generation.id', read_only=True)
    evolves_from_species_id = serializers.IntegerField(source='species.evolves_from_species_id', read_only=True)
    evolution_chain_id = serializers.IntegerField(source='species.evolution_chain_id', read_only=True)
    habitat_id = serializers.IntegerField(source='species.habitat_id', read_only=True)
    gender_rate = serializers.IntegerField(source='species.gender_rate', read_only=True)
    capture_rate = serializers.IntegerField(source='species.capture_rate', read_only=True)
    base_happiness = serializers.IntegerField(source='species.base_happiness', read_only=True)
    is_baby = serializers.BooleanField(source='species.is_baby', read_only=True)
    hatch_counter = serializers.IntegerField(source='species.hatch_counter', read_only=True)
    has_gender_differences = serializers.BooleanField(source='species.has_gender_differences', read_only=True)
    growth_rate_id = serializers.IntegerField(source='species.growth_rate_id', read_only=True)
    forms_switchable = serializers.BooleanField(source='species.forms_switchable', read_only=True)
    conquest_order = serializers.IntegerField(source='species.conquest_order', read_only=True)

    # Write-only fields for foreign keys
    color_id = serializers.PrimaryKeyRelatedField(queryset=PokemonColor.objects.all(), source='species.color', write_only=True)
    shape_id = serializers.PrimaryKeyRelatedField(queryset=PokemonShape.objects.all(), source='species.shape', write_only=True)
    generation_id_post = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all(), source='species.generation', write_only=True)

    class Meta:
        model = Pokemon
        fields = [
            'id',
            'identifier', 
            'generation_id', 
            'evolves_from_species_id', 
            'evolution_chain_id', 
            'color', 
            'shape_id', 
            'habitat_id', 
            'gender_rate', 
            'capture_rate', 
            'base_happiness', 
            'is_baby', 
            'hatch_counter', 
            'has_gender_differences', 
            'growth_rate_id', 
            'forms_switchable', 
            'order', 
            'conquest_order', 
            'height', 
            'weight', 
            'base_experience', 
            'is_default', 
            'color_id', 
            'shape_id', 
            'generation_id_post'
        ]
        extra_kwargs = {
            'color_id': {'write_only': True},
            'shape_id': {'write_only': True},
            'generation_id_post': {'write_only': True},
        }