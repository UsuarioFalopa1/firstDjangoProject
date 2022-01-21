from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from persons.models import Person

# Create your views here.
def welcome(request):
    #return HttpResponse('Hello World from Django')
    #get base de datos, cant personas
    person_numb = Person.objects.count()
    persons = Person.objects.all()
    return render(request, 'welcome.html', {'person_numb': person_numb, 'persons':persons})