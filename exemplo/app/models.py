from django.db import models
# Create your models here.

class Musica(models.Model):
    musica = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    anoPublicacao = models.IntegerField()
