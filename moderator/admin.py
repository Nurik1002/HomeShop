from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from moderator.models import MainUser

admin.site.register(Group)
admin.site.register(Group, GroupAdmin)
class MainUserAdmin(UserAdmin):
    ''' Asosoy userlari '''
    list_display = ['username', 'last_name', 'first_name', 'email', 'is_active', 'is_staff', 'is_superuser']
admin.site.register(MainUser, MainUserAdmin)

