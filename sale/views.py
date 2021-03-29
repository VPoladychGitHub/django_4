from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.cache import cache_page

from django_4 import settings
from sale.models import City, Provider

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def index(request):
    return HttpResponse("Hello, world. You're at the sale index.")


class CityDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = City
    fields = ['name', 'number_inhabitants']


class CityListView(generic.ListView):
    """Generic class-based view for a list of cities."""
    model = City
    paginate_by = 30


@cache_page(CACHE_TTL)
def listing(request):
    city_list = City.objects.all()
    print(type(city_list))
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    # q = QuerySet(my_dict)
    # for i in q:
    #     print(str(i))
    #print(q)
    paginator = Paginator(city_list, 30)  # Show 30 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sale/city_list.html', {'page_obj': page_obj})


class CityCreate(PermissionRequiredMixin, generic.CreateView):
    model = City
    fields = '__all__'  # Not recommended (potential security issue if more fields added)


class CityUpdate(PermissionRequiredMixin, generic.UpdateView):
    model = City
    fields = ['name', 'number_inhabitants']


class CityDelete(PermissionRequiredMixin, generic.DeleteView):
    model = City
    success_url = reverse_lazy('cities')


class ProviderCreate(generic.CreateView):
    model = Provider
    fields = '__all__'  # Not recommended (potential security issue if more fields added)
