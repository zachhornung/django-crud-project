from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Snack
from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
  template_name = 'home.html'
  
class AboutView(TemplateView):
  template_name = 'about.html'
  
class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snack
  
class SnackDetailView(DetailView):
  template_name = 'snack_detail.html'
  model = Snack
  
class SnackCreateView(CreateView):
  model = Snack
  template_name = "snack_create.html"
  fields = ["name", "purchaser", "description"]
    
class SnackUpdateView(UpdateView):
  model = Snack
  template_name = "snack_update.html"
  fields = ["name", "purchaser", "description"]
  
class SnackDeleteView(DeleteView):
    model = Snack
    template_name = "snack_delete.html"
    success_url = reverse_lazy("snack_list")