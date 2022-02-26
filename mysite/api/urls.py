from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('posts', PostsViewSet, basename='posts')

urlpatterns = [
    path('',TimelineView.as_view()),
    path('',include(router.urls)),
    path('login/', obtain_auth_token),
    path('user/', UserView.as_view()),
    path('user/<str:obj>', UserView.as_view()),
    path('register/', RegisterView.as_view()),
    path('question/', QuestionsView.as_view()),
    path('question/<int:pk>', QuestionsView.as_view()),
    path('followtag/', TagView.as_view())
]