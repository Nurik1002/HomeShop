from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from home.models import Home


def home_list(request):
    data = Home.objects.all()
    return render(request, 'home.html', data)

def home_detail(request, id):
    data = Home.objects.get(id = id)
    return render(request, 'home/home_detail.html', data)


