from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from logbook.models import Event

def index(request):
    template = loader.get_template('index.html')

    events = Event.objects.order_by('entryDate').reverse()

    context = RequestContext(request, {
        'events': events,
    })

    return HttpResponse(template.render(context))
