from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from sale.models import City, Provider



def index(request):
    return HttpResponse("Hello, world. You're at the sale index.")


class CityDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = City
    fields = ['name', 'number_inhabitants']


class CityListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = City
    paginate_by = 10


class CityCreate(PermissionRequiredMixin, generic.CreateView):
    model = City
    fields = '__all__'  # Not recommended (potential security issue if more fields added)
    permission_required = 'sale.can_mark_returned'


class CityUpdate(PermissionRequiredMixin, generic.UpdateView):
    model = City
    fields = ['name', 'number_inhabitants']
    permission_required = 'sale.can_mark_returned'


class CityDelete(PermissionRequiredMixin, generic.DeleteView):
    model = City
    success_url = reverse_lazy('cities')
    permission_required = 'sale.can_mark_returned'



class ProviderCreate(generic.CreateView):
    model = Provider
    fields = '__all__'  # Not recommended (potential security issue if more fields added)
# permission_required = 'sale.can_mark_returned'
