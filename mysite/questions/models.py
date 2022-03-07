from django.db import models
from django.contrib.auth.models import User
from hashtag.models import Hashtag

class Questions(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=140, null=True)
    desc = models.TextField(null=True)
    attachment = models.FileField(upload_to='posts/', null=True)
    hashtag = models.ManyToManyField(Hashtag, related_name="questionhashtag")

    def __str__(self):
        return self.title

class Answer(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=140, null=True)
    desc = models.TextField(null=True)
    attachment = models.FileField(upload_to='posts/', null=True)

