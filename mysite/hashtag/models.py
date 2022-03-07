import imp
from django.db import models
from django.contrib.auth.models import User

def superuser(): return User.objects.filter(is_superuser=True)

class Hashtag(models.Model):
    username = models.ForeignKey(User, on_delete=superuser, null=True)
    name = models.CharField(max_length=12, primary_key=True)
    desc = models.TextField()
    # follower = models.ManyToManyField(User, related_name="tagfollower")
    
    def __str__(self):
        return self.name

class TagFollow(models.Model):
    name = models.ManyToManyField(Hashtag, related_name='tag_name', null=True)
    follower = models.ManyToManyField(User, related_name='tag_follower_name', null=True)
    checkunique = models.CharField(max_length=50, unique=True)
