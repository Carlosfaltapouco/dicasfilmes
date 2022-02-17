from datetime import datetime
from pickle import TRUE
from django.db import models

class Dica(models.Model):
    nome_da_dica = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    onde =  models.CharField(max_length=200)
    comentario= models.TextField()
    date_dica = models.DateTimeField(default=datetime.now, blank=TRUE)