from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render
from persons.forms import PersonForm
from persons.models import Person


# Create your views here.
def personDetails(request, id):
    #person = Person.objects.get(pk=id)
    person = get_object_or_404(Person, pk=id)
    return render(request, 'persons/details.html', {'person': person})

#PersonForm = modelform_factory(Person, exclude=[])

def newPerson(request):
    if request.method == "POST":
        formPerson = PersonForm(request.POST)
        if formPerson.is_valid():
            formPerson.save()
            return redirect("index")
    else:
        formPerson = PersonForm()

    return render(request, 'persons/new.html', {'formPerson': formPerson})