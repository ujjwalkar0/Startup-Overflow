from rest_framework.serializers import ModelSerializer
from questions.models import Questions

class QuestionsSerializer(ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'
