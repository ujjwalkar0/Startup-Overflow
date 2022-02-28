from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.CharField(max_length=250)
    mobile_no = models.IntegerField(null=True)
    entre = models.BooleanField(default=False)
    mentor = models.BooleanField(default=False)
    inventor = models.BooleanField(default=False)
    job_seaker = models.BooleanField(default=False)

    def __str__(self):
        return self.username.username

class Education(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name    

class Hobbies(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Hashtag, on_delete=models.CASCADE, related_name='hobby_name', null=True)

    def __str__(self):
        print(self.name)
        return self.name.name 

class Skills(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ManyToManyField(Hashtag, related_name='skill_name')

    def __str__(self):
        return self.name    

class Interests(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ManyToManyField(Hashtag, related_name='interest_name')

    def __str__(self):
        return self.name    
