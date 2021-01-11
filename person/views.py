from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.response import TemplateResponse
from django.urls import reverse

from person.forms import PersonalModelForm
from person.models import Person
from django.views import generic


def index(request):
    return HttpResponse("Hello, world. You're at the person index.")


def index2(request):
    context = {}
    return TemplateResponse(request, "person/index.html", context=context)


def person_edit(request, pk):
    person_instance = get_object_or_404(Person, pk=pk)
    if request.method == "GET":
        form = PersonalModelForm(instance=person_instance)
    else:
        form = PersonalModelForm(request.POST, instance=person_instance)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('person-update', pk=pk)

    return render(
        request,
        "person/person_form.html",
        context={
            "form": form,
        }
    )


def new_person(request):
    if request.method == "GET":
        form = PersonalModelForm()
    else:
        form = PersonalModelForm(request.POST)
        if form.is_valid():
            saved_form = form.save()
            return redirect('person-create')

    return render(
        request,
        "person/person_form.html",
        context={
            "form": form,
        }
    )


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
