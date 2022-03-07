from django.urls import path
from hashtag.views import *

urlpatterns = [
    path('tag/', TagView.as_view()),
    path('tag/<str:pk>/', TagView.as_view())
]