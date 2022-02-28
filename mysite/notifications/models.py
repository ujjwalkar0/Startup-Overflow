from django.db import models

class Notification(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    noti = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.noti