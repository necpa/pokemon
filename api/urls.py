from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet

router = DefaultRouter()
router.register(r'pokemon', PokemonViewSet)  # /api/pokemon/

urlpatterns = router.urls