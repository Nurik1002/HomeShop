from django.urls import path
from home import views

urlpatterns = [
    path('', views.home_list, name='home'),
    path('<int:pk>/', views.home_detail, name="detail"),
    path('create/<int:id>', views.home_create , name="create"),
]
