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

#class AdFormView(FormView):
#    template_name = 'search.html'
#    form_class = AdSearchForm
#
#    def form_valid(self, form):
#        import pdb; pdb.set_trace()
#

def search(request):
    form = AdSearchForm(request.POST or {})
    if form.is_valid():
        if form.data['race']:
           results = Ad.objects.filter(race=form.data['race'], 
                              candidate_or_initiative=form.data['candidate_or_initiative'],
                              support_oppose=form.data['support_oppose']
                             )
        else:
           results = Ad.objects.filter( 
                              candidate_or_initiative=form.data['candidate_or_initiative'],
                              support_oppose=form.data['support_oppose']
                             )
        results_header = "Results:"
    else:
        results = Ad.objects.none()
        results_header = ""

    return render(request, 'search.html', {
       'form': form,
       'results': results,
       'results_header': results_header
    })
