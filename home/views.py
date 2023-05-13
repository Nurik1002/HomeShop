from typing import Optional
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from moderator.models import MainUser
from home.models import Home
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from .forms import HomeFilterForm, HomeForm


def home_list(request):
	context = {}
	data = Home.objects.all()
	context["data"] = data

	return render(request, 'home.html', context)
    


def search(request):  
    context = {}
    query = request.GET.get("q")
    data = Home.objects.filter(
        Q(title__icontains=query) | Q(city__icontains=query) | Q(address__icontains=query) | Q(price__icontains=query) | Q(description__icontains=query)
    )
    context['data'] = data
    return render(request, "home.html", context)


# def get_region(request, region):	
# 	context = {}
# 	data = Home.objects.filter(city = region)
# 	context['data'] = data
# 	return render(request, "home/home_reg.html", context)



def home_filter(request):
    if request.method == 'GET':
        form = HomeFilterForm(request.GET)
        if form.is_valid():
            city = form.cleaned_data['city']
            homes = Home.objects.filter(city=city)
            return render(request, 'home/home_reg.html', {'data': homes, 'forma': form})
    else:
        form = HomeFilterForm()
    return render(request, 'base.html', {'forma': form})



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
	template_name = "home/home_create.html"
	fields = ('title','price','photo','city', 'address', 'num_of_rooms', 'area', 'description')
	success_url = reverse_lazy("home")

	def test_func(self):
		return self.request.user.is_active
	

	def form_valid(self, form):
		form.instance.user = self.request.user 
		form.save()
		messages.success(self.request, "The task was created successfully.")
		return super().form_valid(form)
	

# forms.py



# views.py



def create_home(request):
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('home')
    else:
        form = HomeForm()
    return render(request, 'home/home_create.html', {'form': form})

	
# class HomeForm(forms.ModelForm):
#     class Meta:
#         model = Home 
#         fields = [
#             'title', 'price', 'photo',
#             'address', 'city', 'num_of_rooms', 'area', 'description'
#         ]
# def home_create(request):
#     form = HomeForm()
#     if request.method == 'POST':
#         form = HomeForm(request.POST, request.FILES)
#         if form.is_valid():
#             object = form.save(commit=False)
#             object.user = request.user
#             object.save()
#             return redirect('home')

#     return render(request, "home/home_create.html", {
#         'form': form,
#     })
	

class HomeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Home
	template_name = 'home/home_delete.html'
	success_url = reverse_lazy('home')
	def test_func(self):
		obj = self.get_object()
		return obj.user == self.request.user


class HomeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Home
    fields = ('title','price', 'photo', 'city', 'address', 'num_of_rooms', 'area', 'description')
    template_name = 'home/home_create.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user