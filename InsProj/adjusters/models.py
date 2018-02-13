from django.db import models

from make_claims.models import Claims

class Adjuster(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    claim = models.ForeignKey('make_claims.Claims', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name

    # id = models.AutoField(primary_key=True)
    # AUTO_INCREMENT = 100