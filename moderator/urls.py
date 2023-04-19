from django.contrib import admin
from django.urls import path
from moderator import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [

	path('login/', user_view.Login, name ='login'),
	path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
	path('register/', user_view.register, name ='register'),

]
