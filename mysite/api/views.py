from xml.dom.expatbuilder import parseString
from django.shortcuts import render
from rest_framework import viewsets, status
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from django.http import Http404
import hashlib
from django.db.utils import IntegrityError

class TimelineView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        followings = Follow.objects.filter(username=request.user)
        hashtags = TagFollow.objects.filter(follower=request.user).values('name')
        posts = Posts.objects.filter(username__in=[i.following.username for i in followings], hashtag__in=[i['name'] for i in hashtags])
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        username = User.objects.filter(username=request.user).first()
        title = request.data["title"]
        desc = request.data["desc"]
        hasht = Hashtag.objects.filter(name__in=request.data["hashtag"])
        # print(hashtag)
        a = Posts.objects.create(
            username = username,
            title = title,
            desc = desc,
            )
        a.hashtag.set(hasht)
        a.save()
        return Response({"Response":"Success"})
    

class TagView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        name = Hashtag.objects.filter(name=request.data['name'])
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

class QuestionsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
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

        # print(question)
        # try:
        #     question.title = request.data["title"],
        # except KeyError:
        #     pass

        # try:
        #     question.desc = request.data["desc"],
        # except KeyError:
        #     pass

        # try:
        #     question.attachment = request.data["attachment"]
        # except KeyError:
        #     pass

        # try:
        #     hashtag = Hashtag.objects.filter(name__in=request.data["hashtag"])
        #     question.hashtag.set(hashtag)
        # except KeyError:
        #     pass

        # question.save()

        # return Response({"Response":"Success"})

class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def get_data(self, username, Model, ModelSerializer):
        try:
            model = Model.objects.filter(username=username).first()
            modelserializer = ModelSerializer(model)
            return modelserializer.data
        except Model.DoesNotExist:
            raise Http404


    def get(self, request, format=None):
        hobbies = Hobbies.objects.filter(username=self.user)
        print(hobbies)
        return Response({
            "user":self.get_data(request.user, User, UserSerializer), 
            "profile":self.get_data(request.user, Profile,ProfileSerializer),
            "hobbies":self.get_data(request.user, Hobbies, HobbiesSerializer)
            })

    def post(self, request, obj=None, format=None):
        if obj == "hobbies":            
            for i in request.data["name"]:
                try:
                    tag = Hashtag.objects.get(name=i)
                    Hobbies.objects.create(
                        username=request.user,
                        name = tag
                    )
                except Hashtag.DoesNotExist:
                    return Response({"Response":f"Create {i} First"})
            return Response({"Response":f"Hobbies Created"})


        if obj == "interests":            
            for i in request.data["name"]:
                try:
                    tag = Hashtag.objects.get(name=i)
                    Interests.objects.create(
                        username=request.user,
                        name = tag
                    )
                except Hashtag.DoesNotExist:
                    return Response({"Response":f"Create {i} First"})
            return Response({"Response":f"Interests Created"})

        if obj == "skills":            
            for i in request.data["name"]:
                try:
                    tag = Hashtag.objects.get(name=i)
                    Skills.objects.create(
                        username=request.user,
                        name = tag
                    )
                except Hashtag.DoesNotExist:
                    return Response({"Response":f"Create {i} First"})
            return Response({"Response":f"Skills Created"})

    def put(self,request):
        user = self.get_object(request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def delete(self, request, obj=None, format=None):
        if obj == "hobbies":            
            for i in request.data["name"]:
                try:
                    tag = Hashtag.objects.get(name=i)
                    a = Hobbies.objects.filter(
                        username=request.user,
                        name = tag
                    )
                    print(a)
                    if a.count()==0:
                        return Response({"Response":f"{i} Not exist"})
                    a.delete()
                except Hashtag.DoesNotExist:
                    return Response({"Response":f"{i} Not exist"})
            return Response({"Response":f"Hobbies Deleted"})


        if obj == "interests":
            flag = 0            
            for i in request.data["name"]:
                try:
                    tag = Hashtag.objects.get(name=i)
                    a = Interests.objects.filter(
                        username=request.user,
                        name = tag
                    )
                    if a.count()==0:
                        flag = 1
                    a.delete()
                except Hashtag.DoesNotExist:
                    return Response({"Response":f"{i} Not exist"})
            if flag==1:
                return Response({"Response":f"Interests Created"})
            else:
                return Response({"Response":f"Interests Not exist"})

        if obj == "skills":            
            for i in request.data["name"]:
                try:
                    tag = Hashtag.objects.get(name=i)
                    a = Skills.objects.filter(
                        username=request.user,
                        name = tag
                    )
                    if a.count()==0:
                        return Response({"Response":f"{i} Not exist"})
                    a.delete()
                except Hashtag.DoesNotExist:
                    return Response({"Response":f"{i} Not exist"})
            return Response({"Response":f"Skills Created"})


class ProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class PostsViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def list(self, request):
        posts = Posts.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Posts.objects.all()
        article = get_list_or_404(queryset, pk=pk)
        serializer = PostSerializer(article)
        return Response(serializer.data)

class RegisterView(APIView):
    # Anyone Can Register
    permission_classes = (permissions.AllowAny,)  
    def post(self, request, format=None):
        # Collect Data from the Form
        username = request.data["username"]
        password = request.data["password"]
        confirm_password = request.data["confirm_password"]
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        email = request.data["email"]


        # Check If username Already exist or Not
        if User.objects.filter(username=username):
            return Response({"Message":"Username Already Exist"})

        # Check If email Already exist or Not
        if User.objects.filter(email=email):
            return Response({"Message":"We already have an user with this email address"})

        # Check If password and Confirm Password same or Not
        if password!=confirm_password:
            return Response({"Message":"Password Not Matched"})

        # Now Create the User
        user = User.objects.create(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
        )

        # Set password for the User
        user.set_password(password)
        
        #Save User to the Database
        user.save()

        return Response({"Message":"User Created"})

class AccountView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404  

    def get(self, request, format=None):
        snippet = self.get_object(request.user.id)
        serializer = UserSerializer(snippet)
        return Response(serializer.data)
    
    # Incomplete
    def put(self, request, format=None):
        me = User.objects.get(username=request.user)
        me.first_name = request.data["first_name"]
        me.last_name = request.data["last_name"]
        email = request.data["email"]


        snippet = self.get_object(request.user.id)

        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        snippet = self.get_object(request.user.id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class UserView(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)

#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404  

#     def get(self, request, pk, format=None):
#         print(request.user.id)
#         snippet = self.get_object(request.user.id)
#         serializer = UserSerializer(snippet)
#         return Response(serializer.data)
    
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(request.user.id)
#         serializer = UserSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(request.user.id)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
