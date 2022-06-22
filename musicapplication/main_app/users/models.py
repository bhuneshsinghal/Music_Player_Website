from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .choices import genderchoice
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50,null=True,blank=True,verbose_name="First Name")
    last_name = models.CharField(max_length=50,null=True,blank=True,verbose_name="Last Name")
    date_of_birth = models.DateField(null=True,blank=True,verbose_name="Birth Date")
    gender = models.CharField(max_length=20,choices=genderchoice.choose,default='Male',verbose_name='Gender')
    auth_token = models.CharField(max_length=200,null=True,blank=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now,verbose_name="Joining Date")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email