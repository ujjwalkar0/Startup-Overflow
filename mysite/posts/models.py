from django.db import models
from django.contrib.auth.models import User
from hashtag.models import Hashtag

class Posts(models.Model):
    username = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=140, null=True)
    desc = models.TextField(null=True)
    attachment = models.FileField(upload_to='posts/', null=True)
    hashtag = models.ManyToManyField(Hashtag, related_name='plans', null=True)
    post_time = models.TimeField(auto_now=True, null=True)
    post_date = models.DateField(auto_now=True, null=True)
    
    def __str__(self):
        return self.title    

class Likes(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True)
    vote = models.TextChoices('vote','Upvote None Downvote')

    def __str__(self):
        return self.posts.title   

class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=220)
    attachment = models.FileField(upload_to='comment/', null=True)

    def __str__(self):
        return self.comment   

class Share(models.Model):
    pass
