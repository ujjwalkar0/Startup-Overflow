from django.shortcuts import render
from rest_framework import viewsets

class ArticleView(viewsets.ViewSet):
    def list(self, request):
        pass