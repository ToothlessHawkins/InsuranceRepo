# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import account, driver, vehicle

# Register your models here.
admin.site.register(account)
admin.site.register(driver)
admin.site.register(vehicle)

