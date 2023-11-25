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
    id = models.IntegerField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=12, )
    emoji = models.CharField(max_length=6)
    