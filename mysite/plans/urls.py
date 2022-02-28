from django.urls import path, include
from plans.views import *

urlpatterns = [
    path('',PlansView.as_view())
]