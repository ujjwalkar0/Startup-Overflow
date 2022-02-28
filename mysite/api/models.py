from django.db import models
from django.contrib.auth.models import User

def superuser(): return User.objects.filter(is_superuser=True)

# Public Profile of A User
class Profile(models.Model):
    """
    In Profile table we are storing bio, usertype of a user, 
    so this have one to one relationship with User table. 
    we are taking username as a primary key of Profile Table.
    """
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.CharField(max_length=250)
    mobile_no = models.IntegerField(null=True)
    entre = models.BooleanField(default=False)
    mentor = models.BooleanField(default=False)
    inventor = models.BooleanField(default=False)
    job_seaker = models.BooleanField(default=False)

    def __str__(self):
        return self.username.username

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
    checkunique = models.CharField(max_length=16, unique=True)

class Follow(models.Model):
    username = models.ForeignKey(User, on_delete=superuser, related_name='follow_to', null=True)
    following = models.ForeignKey(User, on_delete=superuser, related_name='followed_by', null=True)
    
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

class Notification(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    noti = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.noti

class Job(models.Model):
    company = models.ManyToManyField(User, related_name='company', null=True)
    jobseaker = models.ManyToManyField(User, related_name='jobseaker', null=True)
    title = models.CharField(max_length=128, null=True)
    desc = models.TextField(null=True)
    hashtag = models.ManyToManyField(Hashtag, related_name='hashtag', null=True)

