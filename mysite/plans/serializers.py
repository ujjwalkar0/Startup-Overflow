import imp
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from plans.models import Plans

class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plans
        fields = '__all__'