from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)

class Person(models.Model):
    name = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    company = models.ForeignKey(Company)

class Project(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company)

class Tag(models.Model):
    name = models.CharField(max_length=200)

class Event(models.Model):
    EVENT_TYPES = (
        (1, 'todo'),
        (2, 'call'),
    )

    description = models.CharField(max_length=200)
    eventType =  models.IntegerField(choices=EVENT_TYPES)
    entryDate = models.DateTimeField()
    dueDate = models.DateTimeField(blank=True)
    person = models.ForeignKey(Person, blank=True)
    company = models.ForeignKey(Company, blank=True)
    project = models.ForeignKey(Project, blank=True)
    tag = models.ForeignKey(Tag, blank=True)

