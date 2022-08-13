from django.db import models

# Create your models here.
class Cadastro(models.Model):
  username = models.CharField(max_length=150)
  email = models.CharField(max_length=100)
  senha = models.CharField(max_length=24)