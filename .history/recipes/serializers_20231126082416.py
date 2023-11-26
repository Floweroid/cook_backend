from rest_framework import serializers
from .models import Recipe, Stuff

class StuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stuff
        fields = ('id', 'type', 'name', 'emoji')

class RecipeSerializer(serializers.ModelSerializer):
    stuff = serializers.SerializerMethodField()
    tools = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'link', 'stuff', 'tools')

    def get_stuff(self, obj):
        return [stuff.name for stuff in obj.stuff.all()]

    def get_tools(self, obj):
        return [tool.name for tool in obj.tools.all()]