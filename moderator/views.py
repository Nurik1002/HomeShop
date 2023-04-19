from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from moderator.forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from django.views.generic import CreateView
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'user/register.html'



# def index(request):
#     return render(request, 'home.html', {'title':'index'})




# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')
#
#             messages.success(request, f'Sizning akkauntingiz yaratildi!')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#         return render(request, 'user/register.html', {'form':form, 'title':'register here'})
#
# def  Login(requset):
#     if requset.method == 'POST':
#         username = requset.POST['username']
#         password = requset.POST['password']
#         user = authenticate(requset, username = username, password = password)
#         if user is not None:
#             form = login(requset, user)
#             messages.success(requset, f"Hush kelibsiz {username}!!!")
#             return redirect('index')
#         else:
#             messages.info(requset, f"Akkaunt topilmadi!!! Iltimos avval ro'yxatdan o'ting!!!")
#     form = AuthenticationForm()
#     return redirect(requset, 'user/login.html', {'form':form, 'title':'log in'})
