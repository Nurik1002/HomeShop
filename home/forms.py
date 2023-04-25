from django.views.generic.edit import CreateView
from home.models import Home 
from django.contrib import messages
from django.urls import reverse_lazy

class CreateHome(CreateView):
	model = Home

	fields = ['title', 'price', 'user', 'photo', 'address', 'city', 'num_of_rooms', 'area']
	success_url = reverse_lazy('home')

	def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "E'lon berildi!")
        return super(CreateHome,self).form_valid(form)
