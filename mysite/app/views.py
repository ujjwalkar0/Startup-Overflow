from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from django.contrib.auth.models import User
import jwt, datetime
from rest_framework import permissions

class HomeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        return Response({"Hello":"World"})

class RegisterView(APIView):
    def post(self, request):
        # print(request.data)
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        email = request.data["email"]
        username = request.data["username"]
        password = request.data["password"]
        confirm_password = request.data["confirm_password"]

        if password!=confirm_password:
            # print("Password Not Matched")
            return Response({"Message":"Password Not Matched"})

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
        )
        # print(user)
        user.save()
        return Response(request.data)


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        print("Hello",request.data)

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256') #.decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # token = request.COOKIES.get('jwt')
        # # return Response({"token":token.encode('utf-8')})
        # if not token:
        #     raise AuthenticationFailed('Unauthenticated!')

        # try:
        #     payload = jwt.decode(token[2:-1], "secret", algorithms=["HS256"])

        # except jwt.ExpiredSignatureError:
        #     raise AuthenticationFailed('Unauthenticated!')

        # user = User.objects.filter(id=payload['id'])
        # serializer = UserSerializer(user)
        # print(user[0].email)
        
        return Response({"Hello":"World"})


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

"""
{
"first_name":"ujjwal",
"last_name":"kar",
"email":"ujjwalkar21@gmail.com",
"username":"ujjwalkar",
"password":"3672@Uk.com",
"confirm_password":"3672@Uk.com",
}

{
    "username":"ujjwalkar",
    "password":"3672@Uk.com"
}

"""