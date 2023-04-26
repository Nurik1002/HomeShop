from django.urls import path
from home import views


urlpatterns = [
	path('<int:pk>/delete', views.HomeDeleteView.as_view(), name = 'delete'),
    path('create/', views.HomeCreateView.as_view() , name="create"),
    path('<int:pk>/', views.home_detail, name="detail"),
    path('', views.home_list, name='home'),
]
