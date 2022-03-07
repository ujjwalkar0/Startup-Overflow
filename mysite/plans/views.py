from django.shortcuts import render
from django.contrib.auth.models import User
from plans.models import *
from plans.serializers import *
from hashtag.models import Hashtag, TagFollow
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *

class PlansView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, pk=None):
        hashtags = TagFollow.objects.filter(follower=request.user).values('name')
        
        if not pk:
            questions = Plans.objects.filter(hashtag__in=[i['name'] for i in hashtags])
            print(questions)
        else:
            questions = Plans.objects.filter(id=pk)

        serializer = PlanSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        username = User.objects.filter(username=request.user).first()
        
        plan = Plans.objects.create(
            username = username,
            title = request.data["title"],
            desc = request.data["desc"],
        )
        try:
            plan.attachment = request.data["attachment"]
        except KeyError:
            pass
        
        plan.hashtag.set(Hashtag.objects.filter(name__in=request.data["hashtag"]))
        plan.save()

        return Response({"Response":"Plan Posted"})
    
