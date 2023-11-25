from django.shortcuts import render
from rest_framework import viewsets


# Create your views here.
# reciepe/views.py


from recipes.models import Recipe, Stuff
from recipes.serializers import RecipeSerializer, StuffSerializer


class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
class StuffsViewSet(viewsets.ModelViewSet):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer
