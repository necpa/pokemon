from rest_framework import serializers
from .models import Pokemon, PokemonSpecies, PokemonColor, PokemonShape, Type

class PokemonSerializer(serializers.ModelSerializer):
    # Read-Write fields for related models
    color = serializers.CharField(source='species.color.identifier', read_only=True)
    shape = serializers.CharField(source='species.shape.identifier', read_only=True)
    evolves_from_species_id = serializers.IntegerField(source='species.evolves_from_species_id', allow_null=True)
    evolution_chain_id = serializers.IntegerField(source='species.evolution_chain_id')
    habitat_id = serializers.IntegerField(source='species.habitat_id')
    gender_rate = serializers.IntegerField(source='species.gender_rate')
    capture_rate = serializers.IntegerField(source='species.capture_rate')
    base_happiness = serializers.IntegerField(source='species.base_happiness')
    is_baby = serializers.BooleanField(source='species.is_baby')
    hatch_counter = serializers.IntegerField(source='species.hatch_counter')
    has_gender_differences = serializers.BooleanField(source='species.has_gender_differences')
    growth_rate_id = serializers.IntegerField(source='species.growth_rate_id')
    forms_switchable = serializers.BooleanField(source='species.forms_switchable')
    conquest_order = serializers.IntegerField(source='species.conquest_order', allow_null=True)

    # Read-Write for foreign keys
    generation_id = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all(), source='species.generation_id')

    # Write fields for foreign keys
    color_id = serializers.PrimaryKeyRelatedField(queryset=PokemonColor.objects.all(), source='species.color', write_only=True)
    shape_id = serializers.PrimaryKeyRelatedField(queryset=PokemonShape.objects.all(), source='species.shape', write_only=True)

    class Meta:
        model = Pokemon
        fields = [
            'id',
            'identifier', 
            'generation_id', 
            'evolves_from_species_id', 
            'evolution_chain_id', 
            'color_id', 
            'shape_id',
            'color', 
            'shape', 
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
            'is_default'
        ]
        extra_kwargs = {
            'color_id': {'write_only': True},
            'shape_id': {'write_only': True},
            'generation_id_post': {'write_only': True},
        }

    def create(self, validated_data):
        """
        Crée un objet Pokemon et son objet PokemonSpecies associé.
        """
        # Extraire les données liées à species
        species_data = validated_data.pop('species', None)

        if not species_data:
            raise serializers.ValidationError({"species": "Ce champ est obligatoire."})
        
        if 'generation_id' in species_data:
            species_data['generation_id'] = species_data['generation_id'].id if species_data['generation_id'] else None

        # Créer d'abord l'objet PokemonSpecies
        species_instance = PokemonSpecies.objects.create(**species_data)

        # Ensuite, créer le Pokémon avec species_instance
        instance = Pokemon.objects.create(species=species_instance, **validated_data)

        return instance

    def update(self, instance, validated_data):
        """
        Met à jour un objet Pokemon et son objet PokemonSpecies associé.
        """
        # Extraire les données liées à species
        species_data = validated_data.pop('species', {})
        print(species_data)

        # Mettre à jour les champs de l'objet Pokemon
        instance.id
        instance.identifier = validated_data.get('identifier', instance.identifier)
        instance.height = validated_data.get('height', instance.height)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.base_experience = validated_data.get('base_experience', instance.base_experience)
        instance.is_default = validated_data.get('is_default', instance.is_default)
        instance.save()

        # Mettre à jour l'objet PokemonSpecies associé
        species_instance = instance.species
        species_instance.evolves_from_species_id = species_data.get('evolves_from_species_id', species_instance.evolves_from_species_id)
        species_instance.evolution_chain_id = species_data.get('evolution_chain_id', species_instance.evolution_chain_id)
        species_instance.habitat_id = species_data.get('habitat_id', species_instance.habitat_id)
        species_instance.gender_rate = species_data.get('gender_rate', species_instance.gender_rate)
        species_instance.capture_rate = species_data.get('capture_rate', species_instance.capture_rate)
        species_instance.base_happiness = species_data.get('base_happiness', species_instance.base_happiness)
        species_instance.is_baby = species_data.get('is_baby', species_instance.is_baby)
        species_instance.hatch_counter = species_data.get('hatch_counter', species_instance.hatch_counter)
        species_instance.has_gender_differences = species_data.get('has_gender_differences', species_instance.has_gender_differences)
        species_instance.growth_rate_id = species_data.get('growth_rate_id', species_instance.growth_rate_id)
        species_instance.forms_switchable = species_data.get('forms_switchable', species_instance.forms_switchable)
        species_instance.conquest_order = species_data.get('conquest_order', species_instance.conquest_order)

        # Gérer les clés étrangères
        if 'generation_id' in species_data:
            species_instance.generation_id = species_data['generation_id'].id if species_data['generation_id'] else None
        if 'color' in species_data:
            species_instance.color = species_data['color'] if species_data['color'] else species_instance.color
        if 'shape' in species_data:
            species_instance.shape = species_data['shape'] if species_data['shape'] else species_instance.shape

        print("Avant sauvegarde species_instance:", vars(species_instance))
        species_instance.save()
        print("Après sauvegarde species_instance")

        return instance