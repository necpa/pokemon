from django.apps import AppConfig
from django.db import connection

def reset_auto_increment():
    """ Met à jour l'auto-incrémentation des IDs pour éviter les conflits. """
    tables = ["pokemon_species", "pokemon"]  # Ajoute ici toutes tes tables

    with connection.cursor() as cursor:
        for table in tables:
            cursor.execute(
                f"SELECT setval(pg_get_serial_sequence('{table}', 'id'), COALESCE(MAX(id), 1) + 1, false) FROM {table};"
            )


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        reset_auto_increment()
