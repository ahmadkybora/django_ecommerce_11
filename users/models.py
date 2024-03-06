import random

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.core import validators
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from rest_framework import serializers
# from utils.validators import validate_phone_number, validate_username

class UserManager(BaseUserManager):
    user_in_migration = True

    def _create_user(self, username, phone_number, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()

        if not username:
            raise ValueError('the given username must be set')
        
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number,
                          username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        
        if not extra_fields.get('no_password'):
            user.set_password(password)

        user.save(using=self._db)
        return user
    
    def create_user(self, username=None, phone_number=None, email=None, password=None, **extra_fields):
        if username is None:
            if email:
                username = email.split('@', 1)[0]

            if phone_number:
                username = random.choice('abcdefghijklmnopqrstuvwxyz') + str(phone_number)[-7:]

            while User.objects.filter(username=username).exists():
                username += str(random.randint(10, 99))
        return self._create_user(username, phone_number, email, password, False, False, **extra_fields)
    
    def create_superuser(self, username, phone_number, email, password, **extra_fields):
        return self._create_user(username, phone_number, email, password, True, True, **extra_fields)
    
    def get_by_phone_number(self, phone_number):
        return self.get(**{ 'phone_number': phone_number })
    
# def validate_username(value):
#     if (value.lower() != 2):
#         raise serializers.ValidationError("Invalid name and age combination.")
#     if (value != "s"):
#         raise serializers.ValidationError("Invalid name and age combination.")
#     return value
    
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=32, unique=True,
                                # help_text=_(
                                #     'Required. 30 ch'
                                # ),
                                # validators=[
                                #     validate_username
                                # ],
                                # error_messages={
                                #     "unique": _("s")                              
                                # }
                                )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True, null=True, blank=True)
    phone_number = models.BigIntegerField(_('mobile number'), unique=True, null=True, blank=True,
                                        #   validators=[
                                        #       validate_phone_number],
                                          error_messages={
                                              'unique': _('A user')
                                          })
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('D'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('DE'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_seen = models.DateTimeField(_('last seen'), null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    class Meta:
        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = _('users')
        