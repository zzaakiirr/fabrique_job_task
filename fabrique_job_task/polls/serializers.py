from datetime import datetime as dt

from rest_framework import serializers

from .models import Poll, Question, Answer
from .serializer_validators import user_existence_validator

# MARK: - Poll serializers

class PollCreateSerializer(serializers.ModelSerializer):
    desc = serializers.CharField(allow_blank=True, required=False)
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def validate_end_date(self, value):
        start_date = dt.strptime(
            self.initial_data.get('start_date'),
            "%Y-%m-%d"
        )
        if start_date and start_date.date() > value:
            raise serializers.ValidationError("End date should be after start")
        return value

    class Meta:
        model = Poll
        fields = '__all__'


class PollDefaultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = '__all__'
        read_only_fields = ('start_date', )

# MARK: - Question serializers

class QuestionSerializer(serializers.ModelSerializer):
    user_identifier = serializers.IntegerField(required=False)

    class Meta:
        model = Question
        fields = '__all__'

# MARK: - Answer serializers

class AnswerSerializer(serializers.ModelSerializer):
    user_identifier = serializers.IntegerField(
        required=False,
        validators=[user_existence_validator]
    )

    class Meta:
        model = Answer
        fields = '__all__'

# MARK: - User polls serializers

class QuestionDummySerializer(serializers.ModelSerializer):
    poll = serializers.IntegerField()

    class Meta:
        model = Question
        fields = '__all__'


class AnswerDummySerializer(serializers.ModelSerializer):
    question = serializers.IntegerField()

    class Meta:
        model = Answer
        fields = '__all__'


class QuestionAnswerSerializer(serializers.Serializer):
    question = QuestionDummySerializer(read_only=True)
    answer = AnswerDummySerializer(read_only=True)


class UserPollsSerializer(serializers.ModelSerializer):
    question_answers = QuestionAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'
