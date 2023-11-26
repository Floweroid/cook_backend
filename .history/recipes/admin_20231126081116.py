# recipes/admin.py
# Register your models here.

from django.contrib import admin
from .models import Recipe, Stuff

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    def display_stuff(self, obj):
        return ', '.join([stuff.name for stuff in obj.stuff.all()]) if obj.stuff.exists() else '-'

    def display_tools(self, obj):
        return ', '.join([tool.name for tool in obj.tools.all()]) if obj.tools.exists() else '-'

    display_stuff.short_description = 'Stuff'  # Custom header name for the column
    display_tools.short_description = 'Tools'  # Custom header name for the column

# Register the Stuff model and the admin class
@admin.register(Stuff) 
# Define the admin class for Stuff
class StuffAdmin(admin.ModelAdmin):
    list_display = ('id','type','name', 'emoji')  # Customize displayed fields in the admin list
    list_filter = ('type',)  # Add a filter for the 'type' field



