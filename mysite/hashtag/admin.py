from django.contrib import admin
from hashtag.models import Hashtag, TagFollow

admin.site.register([
    Hashtag,
    TagFollow
])