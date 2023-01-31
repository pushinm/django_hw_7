from django.contrib import admin
from .models import Person, Child, PersonsRelationShip
# Register your models here.

admin.site.register(Person)
admin.site.register(PersonsRelationShip)
admin.site.register(Child)