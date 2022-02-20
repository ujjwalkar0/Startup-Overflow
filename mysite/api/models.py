from django.db import models

class Posts(models.Model):
    posted_by = models.IntegerField()
    desc = models.TextField()