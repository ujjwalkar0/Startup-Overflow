from django.db import models
from django.contrib.auth.models import User


class GroupName(models.Model):
    name = models.CharField(max_length=40)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    member = models.ManyToManyField(User, related_name='member', null=True)

    def __str__(self):
        return self.name

class GroupMessage(models.Model):
    sender = models.ManyToManyField(GroupName, related_name='groupsender')
    reciever = models.ManyToManyField(User, related_name='groupreciever')
    message = models.CharField(max_length=256)

    def __str__(self):
        return self.message

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', null=True)
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever', null=True)
    message = models.CharField(max_length=256)

    def __str__(self):
        return self.message



# class Group(models.Model):
#     name = models.ForeignKey(GroupName, on_delete=models.CASCADE, related_name='groupname', null=True)
#     # admin = models.ManyToManyField(User, related_name='admin', null=True)
#     member = models.ManyToManyField(User, related_name='member', null=True)
#     message = models.CharField(max_length=256, null=True)

#     def __str__(self):
#         return self.name
