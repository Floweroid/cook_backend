from django.db import models

class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('normal', 'Normal'),
        ('hard', 'Hard'),
    ]

    name = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    stuff = models.TextField()
    emojis = models.TextField(blank=True, null=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='', blank=True)
    tags = models.TextField(blank=True, null=True)
    methods = models.TextField(blank=True, null=True)
    tools = models.TextField()

    def __str__(self):
        return self.name
    
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
    