from dataclasses import field
import imp
from operator import mod
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'date_joined',
            'last_login'
        ]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('username',)

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'

class HobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbies
        fields = '__all__'