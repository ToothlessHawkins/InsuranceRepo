from django.db import models

"""IMPORT CLAIM MODEL FROM CLAIMS APP HERE"""
# from claims.models import Claim

class Adjuster(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    # claim = models.ForeignKey('Claim', on_delete=models.CASCADE,)
    def __str__(self):
        return self.name

    # id = models.AutoField(primary_key=True)
    # AUTO_INCREMENT = 100