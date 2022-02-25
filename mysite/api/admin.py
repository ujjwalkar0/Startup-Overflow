from django.contrib import admin
from .models import *

admin.site.register([
    TagFollow,
    Posts,
    Follow,
    Profile, 
    Message, 
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
    Group,
    Notification,
    Job,
    Plans,
    ])
# admin.site.register(Message)