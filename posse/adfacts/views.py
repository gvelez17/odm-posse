from django.shortcuts import render
from django.views import generic

# Create your views here.

class OrgListView(generic.ListView):
    model = Org

class AdListView(generic.ListView):
    model = Ad

class OrgDetailView(generic.DetailView):
    model = Org

class AdDetailView(generic.DetailView):
    model = Ad
