from django.contrib import admin
from logbook.models import Event
from logbook.models import Company
from logbook.models import Person
from logbook.models import Project
from logbook.models import Tag

admin.site.register(Event)
admin.site.register(Company)
admin.site.register(Person)
admin.site.register(Project)
admin.site.register(Tag)
