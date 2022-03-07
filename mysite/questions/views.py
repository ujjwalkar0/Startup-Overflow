from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from hashtag.models import TagFollow, Hashtag
from questions.models import Questions
from questions.serializers import QuestionsSerializer

class QuestionsView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request,pk=None, format=None):
        hashtags = TagFollow.objects.filter(follower=request.user).values('name')
        if not pk:
            questions = Questions.objects.filter(hashtag__in=[i['name'] for i in hashtags])
            print(questions)
        else:
            questions = Questions.objects.filter(id=pk)

        serializer = QuestionsSerializer(questions, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        hashtag = Hashtag.objects.filter(name__in=request.data["hashtag"])
        a = Questions.objects.create(
            username = request.user,
            title = request.data["title"],
            desc = request.data["desc"],
            attachment = request.data["attachment"]
        )
        a.hashtag.set(hashtag)
        a.save()
        return Response({"Response":"Data Saved"})
    

    def put(self,request,pk,format=None):
        question = Questions.objects.get(id=pk)
        serializer = QuestionsSerializer(question, data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
