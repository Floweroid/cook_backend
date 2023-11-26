from django.db import models

class Stuff(models.Model):
    STUFF_TYPE_CHOICES = [
        ('meat', 'meat'),
        ('vegi', 'vegetable'),
        ('staple', 'staple'),
        ('tools','tools')
    ]
    type = models.CharField(max_length=10, choices=STUFF_TYPE_CHOICES, default='', blank=True)
    name = models.CharField(max_length=12, unique= True)
    emoji = models.CharField(max_length=6)
    
    def __str__(self):
            return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=64)
    link = models.URLField(blank=True, null=True)
    stuff = models.ManyToManyField(Stuff, related_name='related_recipes', limit_choices_to={'type__in': ['meat', 'vegi', 'staple']})
    tools = models.ManyToManyField(Stuff, related_name='tool_recipes', limit_choices_to={'type': 'tools'})

    def __str__(self):
        return self.name
    
    # emojis = models.TextField(blank=True, null=True)
    
    # DIFFICULTY_CHOICES = [
    #     ('easy', 'Easy'),
    #     ('normal', 'Normal'),
    #     ('hard', 'Hard'),
    # ]
    
    # difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='', blank=True)
    # tags = models.CharField(blank=True, null=True)
    # methods = models.TextField(blank=True, null=True)
