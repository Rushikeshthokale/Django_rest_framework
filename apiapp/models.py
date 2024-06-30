from django.db import models

# Create your models here.
class Employe(models.Model):
    name=models.CharField(max_length=20)
    dept=models.CharField(max_length=10)
    salary=models.IntegerField()