from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse



class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)


    class Meta:
        swappable = 'AUTH_USER_MODEL'


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    departement = models.CharField(max_length=100)
    filiere = models.CharField(max_length=100)
    encadrant = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

          


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return str(self.message)



class DeleteRequest(models.Model):
    delete_request = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.delete_request


class Feedback(models.Model):
    feedback = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.feedback












