from django.shortcuts import render
from django.views import generic
from .forms import AdSearchForm
from django.views.generic.edit import FormView

from adfacts.models import Org, Ad

# Create your views here.

class OrgListView(generic.ListView):
    model = Org

class AdListView(generic.ListView):
    model = Ad

class OrgDetailView(generic.DetailView):
    model = Org

class AdDetailView(generic.DetailView):
    model = Ad

class AdFormView(FormView):
    template_name = 'search.html'
    form_class = AdSearchForm

    def form_valid(self, form):
        import pdb; pdb.set_trace()


def search(request):
    form = AdSearchForm(request.GET or {})
    if form.is_valid():
        results = form.get_queryset()
    else:
        results = Ad.objects.none()

    return render(request, 'search.html', {
       'form': form,
       'results': results,
    })
