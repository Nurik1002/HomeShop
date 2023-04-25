from django.urls import path
from home import views
from home.forms import CreateHome

urlpatterns = [
    path('', views.home_list, name='home'),
    path('<int:pk>/', views.home_detail, name="detail"),
    path('create/<int:id>/', CreateHome.as_view() , name="create"),
]
