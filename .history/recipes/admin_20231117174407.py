# recipes/admin.py
# Register your models here.

from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'created_at')  # Fields to display in the list view
#     list_filter = ('author', 'created_at')  # Filters displayed in the right sidebar
#     search_fields = ('title', 'author__username')  # Enable search functionality

#     fieldsets = (
#         (None, {
#             'fields': ('title', 'author', 'created_at')  # Fields to display in detail view
#         }),
#         ('Additional Information', {
#             'fields': ('description', 'difficulty', 'tags', 'methods', 'tools'),
#             'classes': ('collapse',)  # Makes these fields collapsible in the admin interface
#         }),
#     )