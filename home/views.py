from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from moderator.models import MainUser
from home.models import Home
from django.views.generic.edit import UpdateView, DeleteView, CreateView


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def home_list(request):
	context = {}
	data = Home.objects.all()
	context["data"] = data

	return render(request, 'home.html', context)
    

@login_required(login_url='login')
def get_region(request):	
	context = {}
	data = Home.objects.filter(city = 'Tashkent')
	context['data'] = data

	return render(request, "home/home_reg.html", context)




@login_required(login_url='login')
def home_detail(request, pk):
	context = {}
	data = Home.objects.get(id = pk)
	context["data"] = data
	return render(request, 'home/home_detail.html', context)




@login_required(login_url='login')
def my_homes(request, id ):
	user =  MainUser.objects.get(id = id)
	context = {}
	data = Home.objects.filter(user = user)
	context['data'] = data
	return render(request, 'home/my_homes.html', context)






class HomeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = Home
	template_name = 'home/home_create.html'
	success_url = reverse_lazy('home')
	fields = ('title', 'price', 'photo', 'city', 'address', 'num_of_rooms', 'area')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		return self.request.user.is_superuser

class HomeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Home
	template_name = 'home/home_delete.html'
	success_url = reverse_lazy('home')

	def test_func(self):
		obj = self.get_object()
		return obj.user == self.request.user

class HomeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Home
    fields = ('title','price', 'photo', 'city', 'address', 'num_of_rooms', 'area')
    template_name = 'home/home_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user







