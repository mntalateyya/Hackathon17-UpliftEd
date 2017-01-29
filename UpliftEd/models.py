from __future__ import unicode_literals

from django.db import models

from django.conf import settings
from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

class MyUserManager(UserManager):
    def create_user(self, username, password, name, bio=''):
        user = self.model(username=username)
        user.set_password(password)
        user.password = password
        user.display_name = name
        user.bio= bio
        user.save()
        return user
 
class Users(AbstractUser):
    username = models.CharField(max_length=16, unique=True)
    display_name = models.CharField(max_length=64)
    reputation = models.IntegerField(default=0)
    bio = models.CharField(max_length=256)
    
    is_active = models.BooleanField(default=True) 
    objects = MyUserManager()
 
    USERNAME_FIELD = 'username'
 
    def get_full_name(self):
        return self.username
 
    def get_short_name(self):
        return self.username  
    

class Playlists(models.Model):
    owner_ID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=32)    
    category = models.CharField(max_length=15)
    rep_index = models.IntegerField()
    thumbnail = models.CharField(max_length=128)
    created_datetime = models.DateTimeField(auto_now=True)

class Videos(models.Model):
    owner_ID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    playlist_ID = models.ForeignKey(Playlists, on_delete=models.CASCADE)
    video_name = models.CharField(max_length=64)
    video_votes = models.IntegerField()
    video_index = models.IntegerField()
    video_link = models.CharField(max_length=64)
    video_discription = models.CharField(max_length=512)
    
class Subscription(models.Model):
    suscriber=models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subscribed_to', on_delete=models.CASCADE)
    suscribed_to=models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subscribers', on_delete=models.CASCADE)
