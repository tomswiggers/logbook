from django.contrib import admin
from logbook.models import Event
from logbook.models import Company
from logbook.models import Person

admin.site.register(Event)
admin.site.register(Company)
admin.site.register(Person)
