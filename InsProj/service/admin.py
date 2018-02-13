from django.contrib import admin

from .models import Request, Mechanic, ServiceRep

admin.site.register(Request)
admin.site.register(Mechanic)
admin.site.register(ServiceRep)