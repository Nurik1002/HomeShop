from  django.views.generic  import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from home.models import Home


class HomeListView(ListView):
    model = Home
    template_name = 'home.html'
