from django.shortcuts import render
from .models import Person
# Create your views here.
def person_view(request, pk) -> render:
    template_ = 'person.html'
    current_person = Person.objects.get(pk=pk)

    persons = Person.objects.all()

    context = {
        'current_person': current_person,
        'persons': persons
    }

    return render(request, template_, context=context)