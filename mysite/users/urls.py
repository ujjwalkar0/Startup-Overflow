import imp
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from users.views import *

urlpatterns = [
    path('login/',obtain_auth_token),
    path('register/',RegisterView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('in/<str:username>/',UserView.as_view()),
    path('type/',UserType.as_view())
]