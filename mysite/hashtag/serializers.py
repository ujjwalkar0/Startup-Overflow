from dataclasses import field
from rest_framework.serializers import ModelSerializer
from hashtag.models import *

class HashtagSerializer(ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['name','desc']

class TagFollowSerializer(ModelSerializer):
    class Meta:
        model = TagFollow
        fields = ['name','follower']
