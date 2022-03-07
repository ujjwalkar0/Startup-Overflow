from django.urls import path
from posts.views import *

urlpatterns=[
    path('comment/',CommentView.as_view()),
    path('commentview/<int:pk>',CommentViewToALL.as_view()),
    path('<str:catagory>/',PostsViewSet.as_view()),
    path('tag/<str:catagory>/',PostByTagView.as_view()),
    path('view/<int:pk>/',PostsViewToALL.as_view())
]