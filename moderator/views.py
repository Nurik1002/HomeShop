from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from moderator.models import MainUser



def signup(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        name = request.POST.get("uname")
        email = request.POST.get("email")
        phone_num = request.POST.get("pnum")
        password = request.POST.get("password")

        new_user = MainUser.objects.create_user(name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.phone_number = phone_num

        new_user.save()
        return redirect("login")

    return render(request, 'user/register.html', {})

def Login(request):
    if request.method == "POST":
        name = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(request, username=name, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            return HttpResponse("Foydalanuvchi topilmadi")

    return render(request, "user/login.html")

@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect("home")