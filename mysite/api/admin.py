from django.contrib import admin
from .models import *

admin.site.register([
    TagFollow,
    Posts,
    Follow,
    Profile, 
    Education, 
    Hobbies,
    Hashtag,
    Skills,
    Interests,
    Likes,
    Comment,
    Share,
    Questions,
    Answer,
    Products,
    Catagory,
    RatingReview,
    Notification,
    Job,
    ])
# admin.site.register(Message)