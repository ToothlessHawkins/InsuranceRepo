from django.contrib import admin

from . import models

class AdjusterAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'claim']
admin.site.register(models.Adjuster, AdjusterAdmin)