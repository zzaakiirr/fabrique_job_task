from rest_framework import serializers

from .models import Poll, Question, Answer

from .serializer_validators import user_existence_validator


class PollCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = '__all__'


class PollDefaultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = '__all__'
        read_only_fields = ('start_date', )


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    user_identifier = serializers.IntegerField(
        required=False,
        validators=[user_existence_validator]
    )

    class Meta:
        model = Answer
        fields = '__all__'
