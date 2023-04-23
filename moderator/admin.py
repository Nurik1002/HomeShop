from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from home.models import Home
from moderator.models import MainUser

admin.site.unregister(Group)

class MainUserAdmin(UserAdmin):
    ''' Asosoy userlari '''
    list_display = ['username', 'last_name', 'first_name', 'email', 'phone_number', 'is_active', 'is_staff', 'is_superuser']
admin.site.register(MainUser, MainUserAdmin)


class HomeAdmin(admin.ModelAdmin):
    '''Uylar'''
    list_display = ['title', 'price', 'user', 'photo', 'address', 'city', 'num_of_rooms', 'area']
admin.site.register(Home, HomeAdmin)