from django.db import models
from django.contrib.auth.models import User


class UserProfile(User):
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    phoneNumber = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.username
