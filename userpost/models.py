from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

import datetime

# Create your models here.


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError("Users must have an email address")

#         user = self.model(
#             email=self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_staffuser(self, email, password):
#         """
#         Creates and saves a staff user with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.is_staff = True
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.is_staff = True
#         user.is_admin = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


# class User(AbstractUser):
# email = models.EmailField(max_length=255, unique=True)
# phone_number = models.CharField(max_length=12, null=True, blank=True)
# address = models.CharField(max_length=255, null=True, blank=True)
# is_admin = models.BooleanField(default=False)
# is_staff = models.BooleanField(default=False)

# USERNAME_FIELD = "email"
# REQUIRED_FIELDS = []  # Email & Password are required by default.

# objects = UserManager()

# def __str__(self):
#     """String for representing the User Model object."""
#     return (
#         f"{self.last_name} {self.first_name}"
#         if self.last_name and self.first_name
#         else self.username
#     )


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email=self.normalize_email(email), password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=254)
    address = models.CharField(max_length=254, null=True)
    create_at = models.DateField(null=True, blank=True, default=datetime.date.today)
    update_at = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, blank=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = MyAccountManager()


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "CustomUser", related_name="posts", on_delete=models.SET_NULL, null=True
    )

    class Meta:
        ordering = ["created_at"]
