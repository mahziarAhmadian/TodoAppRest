from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.utils.translation import gettext_lazy as _


# Create your models here.

class UserManager(BaseUserManager):
    '''
    Custom user model manager where email is the uniqe identifiers for authentication instead od username.
    '''

    def create_user(self, phone_number, password, **extra_fields):
        '''
        create and save a user with the gven email and password and extra data .
        '''
        if not phone_number:
            raise ValueError(_('The email must be set'))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        '''
        create and save a Superuser with the given email and password .
        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('superuser must have is_staf = true'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('superuser must have is_superuser = true'))
        return self.create_user(phone_number, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    '''
    Custom User MMOdel for our app
    '''
    phone_number = models.CharField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.phone_number
