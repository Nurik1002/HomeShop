from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from moderator.models import MainUser
from home.models import Home


def home_list(request):
	context = {}
	data = Home.objects.all()
	context["data"] = data

	return render(request, 'home.html', context)
    


def home_detail(request, pk):
	context = {}
	data = Home.objects.get(id = pk)
	context["data"] = data
	return render(request, 'home/home_detail.html', context)



@login_required(login_url='login')
def home_create(request, id):
	if request.method == "POST":
		title = request.POST.get("title")
		price = request.POST.get('price')
		photo = request.POST.get('photo')
		address = request.POST.get('address')
		city = request.POST.get('city')
		num_of_rooms = request.POST.get('numofrooms')
		area = request.POST.get('area')

		user = MainUser.objects.get(id = id)

		new_home = Home()
		new_home.title = title
		new_home.price = price
		new_home.user = user
		new_home.photo = photo
		new_home.address = address
		new_home.city = city
		new_home.num_of_rooms = num_of_rooms
		new_home.area = area

		new_home.save()
		return redirect(request, "detail/<int:new_home.id>", {})




	return render(request, "home/home_create.html", {}) 


