from django.contrib import admin
from posts.models import *

admin.site.register([
    Posts,
    Comments
])