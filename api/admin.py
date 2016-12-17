from django.contrib import admin

# Register your models here.

from .models import Map, Route

admin.site.register(Map)
admin.site.register(Route)