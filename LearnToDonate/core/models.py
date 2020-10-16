from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES = (
    ('N', 'Novel'),
    ('F', 'Fiction'),
    ('NF', 'Non Fiction'),
    ('Sc', 'Science'),
    ('M', 'Math'),
    ('AS', 'Applied Science'),
    ('O', 'Other')
)

class UserProfileInfo(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='user_pics/')

class Book(models.Model):
    name = models.CharField(max_length=256)
    category = models.CharField(max_length=2 , choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='bookpics/')
