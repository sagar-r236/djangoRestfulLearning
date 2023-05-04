from django.contrib import admin

# Register your models here.
from home.models import Color, Person

admin.site.register(Color)
admin.site.register(Person)