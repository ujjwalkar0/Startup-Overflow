from hashtag.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import hashlib
from django.db.utils import IntegrityError
from hashtag.serializers import *

class TagView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, pk=None, format=None):
        if pk is None:
            hashtag = Hashtag.objects.all()
            serializer = HashtagSerializer(hashtag, many=True)
            return Response(serializer.data)
        else:
            hashtag = Hashtag.objects.get(name=pk)
            print(hashtag)
            followers = TagFollow.objects.filter(name=hashtag).values('tag_follower_name')
            # print([i['name'] for i in followers])
            print(followers)
            users = User.objects.filter(username__in=followers)
            print(users)
            serializer = TagFollowSerializer(followers, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        name = Hashtag.objects.filter(name=request.data['hashtag'])
        print(name)
        if not name:
            return Response({"Response":"Hashtag Does Not Exist"})
        follower = User.objects.filter(username=request.user)
        hashvalue = str(follower)+str(name)
        print(hashvalue)
        checkunique = hashlib.md5(hashvalue.encode())
        print(checkunique.hexdigest())
        try:
            a = TagFollow.objects.create(checkunique=checkunique.hexdigest())
            a.follower.set(follower)
            a.name.set(name)
            a.save()
            return Response({"Response":"Success"})
        except IntegrityError:
            return Response({"Response":"Already Followed"})

