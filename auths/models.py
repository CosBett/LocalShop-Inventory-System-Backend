from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    
    REQUIRED_FIELDS =[]
    
    def __str__(self):
        return self.username

    # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    # def create_auth_token(sender, instance=None, created=False, **kwargs):
    #     if created:
    #         Token.objects.create(user=instance)


class Admin(models.Model):
    user = models.OneToOneField(
    User, on_delete=models.CASCADE, related_name='admin')
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Clerk(models.Model):
    user = models.OneToOneField(
    User, on_delete=models.CASCADE, related_name='clerk')
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username


