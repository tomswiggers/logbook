from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, related_name='projects')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Event(models.Model):
    EVENT_TYPES = (
        (1, 'meeting'),
        (2, 'call'),
        (3, 'task'),
        (4, 'note')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    eventType =  models.IntegerField(choices=EVENT_TYPES)
    entryDate = models.DateTimeField()
    dueDate = models.DateTimeField(null=True, blank=True)
    person = models.ForeignKey(Person, null=True, blank=True)
    company = models.ForeignKey(Company, null=True, blank=True)
    project = models.ForeignKey(Project, related_name='events', null=True, blank=True)
    tag = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return u'%s' % (self.description)

    def get_eventType_css(self):
        LABELS = [
            'primary',
            'success',
            'warning',
            'info'
        ]

        return LABELS[self.eventType-1]
