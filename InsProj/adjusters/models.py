from django.db import models

"""IMPORT CLAIM MODEL FROM CLAIMS APP HERE"""
# from claims.models import Claims

class Adjuster(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    # claim = models.ForeignKey('Claims', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

    # id = models.AutoField(primary_key=True)
    # AUTO_INCREMENT = 100