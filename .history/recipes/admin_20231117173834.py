# recipes/admin.py
# Register your models here.

from django.contrib import admin

from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # Define any customizations for how the model is displayed in the admin panel
    list_display = ('title', 'author', 'created_at')  # Example fields to display in the list view
    search_fields = ('title', 'author__username')  # Example fields to enable search functionality
    # Add more configurations as needed