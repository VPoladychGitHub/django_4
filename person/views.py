from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from person.forms import PersonalModelForm
from person.models import Person
from django.views import generic


def index(request):
    return HttpResponse("Hello, world. You're at the person index.")


class PersonCreate(generic.CreateView):
    model = Person
    fields = '__all__'  # Not recommended (potential security issue if more fields added)
    initial = {'email': 'test@test.com'}
    permission_required = 'person.can_mark_returned'


class PersonUpdate(generic.UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'email']
    permission_required = 'person.can_mark_returned'


class PersonListView(generic.ListView):
    """Generic class-based list view for a list of authors."""
    model = Person
    paginate_by = 10
