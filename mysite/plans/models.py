from django.db import models
from hashtag.models import Hashtag, superuser
from django.contrib.auth.models import User

class Plans(models.Model):
    username = models.ForeignKey(User, on_delete=superuser)
    title = models.CharField(max_length=128)
    desc = models.TextField()
    hashtag = models.ManyToManyField(Hashtag, related_name='hashplans')
    attachment = models.FileField(upload_to='plans/', null=True)
    accept = models.ForeignKey(User, on_delete=superuser, related_name='accept', null=True)
