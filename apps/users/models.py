# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.db import models

#administrador de los usuarios
class UserManager(BaseUserManager):
    # 
    def _create_user(self,username, email,password,is_staff,is_superuser,**extra_fields):
        if not email:   
            raise ValueError('El email debe ser obligatorio') # lanzamiento de error
        email = self.normalize_email(email) # normaliza el email poniendolo todo a minuscula
        user = self.model(username=username, email=email, is_active=True, is_staff=is_staff,is_superuser=is_superuser,**extra_fields)
        user.set_password(password)
        user.save(using = self.db)  #se le indica que debe de guardar el usuario en la base de datos que se configuro
        return user

    #  funcion para crear los usuarios comunes
    def create_user(self,username,email,password=None,**extra_fields):
        return self._create_user(username,email,password,False,False,**extra_fields)

    # funcion para crear super usuarios
    def create_superuser(self,username,email,password,**extra_fields):
        return self._create_user(username,email,password,True,True,**extra_fields)



class CustomUser(AbstractBaseUser,PermissionsMixin):
    # add additional fields in here
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    apodo = models.CharField(max_length=10, default='')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # intermediario entre cada modelo, se podria decir que es el manager de cada modelo
    objects = UserManager()

    USERNAME_FIELD = 'username' # variable que se definira como username
    REQUIRED_FIELDS = ['email']  # variables requeridas al momento de crear el usuario y superusuario

    # def __str__(self):
    #     return self.email

    def get_short_name(self):
        return self.username