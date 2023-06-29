from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(blank=False, max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(blank=False)
    href = models.CharField(blank=False, max_length=200)