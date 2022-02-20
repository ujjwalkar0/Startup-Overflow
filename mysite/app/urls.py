from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('home/', HomeView, basename='home')
router.register('register/', RegisterView, basename='register')
router.register('login/', LoginView, basename='login')
router.register('user/', UserView, basename='user')
router.register('logout/', LogoutView, basename='logout')

urlpatterns = [
    path('',include(router.urls)),
]

# [
#     path('home/', HomeView.as_view()),
#     path('register/', RegisterView.as_view()),
#     path('login/', LoginView.as_view()),
#     path('user/', UserView.as_view()),
#     path('logout/', LogoutView.as_view()),
# ]