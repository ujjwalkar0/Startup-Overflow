from django.db import models
from django.contrib.auth.models import User
from hashtag.models import Hashtag

class Posts(models.Model):
    username = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    short_desc = models.CharField(max_length=500, default=None)
    desc = models.TextField()
    catagory = models.CharField(max_length=50,default="Article")
    attachment = models.ImageField(upload_to='posts/', null=True)
    hashtag = models.ManyToManyField(Hashtag, related_name='plans')
    post_time = models.TimeField(auto_now=True, null=True)
    post_date = models.DateField(auto_now=True, null=True)
    
    def __str__(self):
        return self.title    
    
    class Meta:
        ordering = ['-id']

class Likes(models.Model):
    username = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE)
    vote = models.TextChoices('vote','Upvote None Downvote')

    def __str__(self):
        return self.posts.title   

class Comments(models.Model):
    username = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment = models.CharField(max_length=220)
    post_time = models.TimeField(auto_now=True, null=True)
    post_date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.comment   

class Share(models.Model):
    pass
