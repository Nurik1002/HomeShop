from django.urls import path
from .views import signup, Login, Logout

urlpatterns = [
    path('signup/', signup ,name='signup'),
    path('login/', Login, name="login"),
    path('logout/', Logout, name="logout"),
]
