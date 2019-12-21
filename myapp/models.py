from django.db import models

# Create your models here.

class Songs(models.Model):
    name = models.CharField(max_length = 100)
    track = models.CharField(max_length = 100)
    length = models.IntegerField()




