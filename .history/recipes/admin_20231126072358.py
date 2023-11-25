# recipes/admin.py
# Register your models here.

from django.contrib import admin
from .models import Recipe, Stuff

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'stuff', 'difficulty','tags','methods','tools','emojis')  # Fields to display in the list view
    list_filter = ('stuff', 'difficulty','tags')  # Filters displayed in the right sidebar
    # search_fields = ('name')  # Enable search functionality

    fieldsets = (
        (None, {
            'fields': ('name', 'stuff', 'link','emojis','difficulty','tags','methods','tools')  # Fields to display in detail view
        }),
        # ('Additional Information', {
        #     'fields': ('description' , 'tags', 'methods', 'tools'),
        #     'classes': ('collapse',)  # Makes these fields collapsible in the admin interface
        # }),
    )
    
    # list_display = ["title", "start_time", "status", "description", "end_time","get_members_display","create_time"]
    # fieldsets = [
    #     (None, {"fields": ["status","title", "description"]}),
    #     ("Date&Time information", {"fields": ["start_time","end_time"], "classes": ["collapse"]}),
    # ]

# Register the Stuff model and the admin class
@admin.register(Stuff) 
# Define the admin class for Stuff
class StuffAdmin(admin.ModelAdmin):
    list_display = ('id','type','name', 'emoji')  # Customize displayed fields in the admin list
    list_filter = ('type',)  # Add a filter for the 'type' field



