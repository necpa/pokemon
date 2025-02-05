from django.db import models

class PokemonColor(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=100)

    class Meta:
        db_table = 'pokemon_colors'

class PokemonShape(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=100)

    class Meta:
        db_table = 'pokemon_shapes'

class PokemonSpecies(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=100)
    generation_id = models.IntegerField(null=True, blank=True)
    evolves_from_species = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    evolution_chain_id = models.IntegerField(null=True, blank=True)
    color = models.ForeignKey(PokemonColor, null=True, blank=True, on_delete=models.SET_NULL)
    shape = models.ForeignKey(PokemonShape, null=True, blank=True, on_delete=models.SET_NULL)
    habitat_id = models.IntegerField(null=True, blank=True)
    gender_rate = models.IntegerField()
    capture_rate = models.IntegerField()
    base_happiness = models.IntegerField()
    is_baby = models.BooleanField()
    hatch_counter = models.IntegerField()
    has_gender_differences = models.BooleanField()
    growth_rate_id = models.IntegerField()
    forms_switchable = models.BooleanField()
    order = models.IntegerField()
    conquest_order = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'pokemon_species'

class Pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=100)
    species = models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    order = models.IntegerField()
    is_default = models.BooleanField()

    class Meta:
        db_table = 'pokemon'

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=100)
    generation_id = models.IntegerField()
    damage_class_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'types'

class PokemonType(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, db_column='id', primary_key=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    slot = models.IntegerField()

    class Meta:
        db_table = 'pokemon_types'
        unique_together = ('pokemon', 'type')
