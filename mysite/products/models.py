from django.db import models

class Products(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=140, null=True)
    image = models.ImageField(upload_to='posts/', null=True)

    def __str__(self):
        return self.title  

class Catagory(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    catagory = models.CharField(max_length=10)

    def __str__(self):
        return self.catagory   

class RatingReview(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    rating = models.IntegerChoices('rating','1 2 3 4 5')
    review = models.CharField(max_length=220)
    attachment = models.FileField(upload_to='review/', null=True)

    def __str__(self):
        return self.catagory   
