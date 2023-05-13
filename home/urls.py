from django.urls import path
from home import views


urlpatterns = [
    path("search/", views.search, name="search_results"),
	path('region/<str:region>', views.get_region, name = 'region' ),
	path('my/<int:id>/', views.my_homes, name = 'my_homes'),
	path('<int:pk>/update', views.HomeUpdateView.as_view(), name = 'update'),
	path('<int:pk>/delete', views.HomeDeleteView.as_view(), name = 'delete'),
    path('create/', views.HomeCreateView.as_view() , name="create"),
    path('<int:pk>/', views.home_detail, name="detail"),
    path('', views.home_list, name='home'),
]
