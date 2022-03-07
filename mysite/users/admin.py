from django.contrib import admin
from users.models import *

admin.site.register([
    Interests,
    Hobbies,
    Skills,
    Profile
])