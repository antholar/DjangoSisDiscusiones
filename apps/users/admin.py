# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# sin esta clase en el administrador no se veria nada de la tabla de usuarios
class CustomUserAdmin(UserAdmin):
    fieldsets = (
    	('CustomUser',{'fields' : ('username','password')}),
    	('Persona Info',{'fields' : ('first_name','last_name','email','apodo')}),
    	('Permissions', {'fields' : ('is_active','is_staff','is_superuser','groups','user_permissions')}),
    )

    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    # model = CustomUser
    # list_display = ['username','email','first_name','last_name','apodo',]

admin.site.register(CustomUser, CustomUserAdmin)