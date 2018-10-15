from django.db import models

# Create your models here.
class Cliente(models.Model):
    email = models.EmailField("email", max_length=200)
    apelido = models.CharField("apelido", max_length=100)
    nome = models.CharField("nome", max_length=100)
    senha = models.CharField("senha", max_length=30)
    celular = models.CharField("celular", max_length=30)
