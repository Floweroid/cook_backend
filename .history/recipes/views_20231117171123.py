from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
# reciepe/views.py


from recipes.models import Recipe
from recipes.serializers import RecipesSerializer


class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipesSerializer