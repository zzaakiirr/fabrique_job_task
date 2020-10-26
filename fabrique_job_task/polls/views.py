from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.status import HTTP_200_OK


from .models import Poll, Question, Answer
from .serializers import (
    PollDefaultSerializer, PollCreateSerializer,
    QuestionSerializer,
    AnswerSerializer,
)


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        query_params = self.request.query_params
        user_identifier = query_params.get('user_identifier')

        if user_identifier:
            user_answers = Answer.objects.filter(user_identifier=user_identifier)
            try:
                questions = [
                    Question.objects.get(pk=answer.question.pk) for answer in user_answers
                ]
            except Question.DoesNotExist:
                return queryset

            poll_pks = set([question.poll.pk for question in questions])

            queryset = queryset.filter(pk__in=poll_pks)

        return queryset

    @action(methods=['get'], url_path="(?P<poll_pk>[^/.]+)/answers",
            url_name='get-user-answers', detail=False)
    def get_user_answers(self, request, poll_pk):
        query_params = self.request.query_params
        user_identifier = query_params.get('user_identifier')

        if user_identifier:
            question_pks = [
                question.pk for question in Question.objects.filter(poll=poll_pk)
            ]
            user_poll_answers = Answer.objects.filter(
                user_identifier=user_identifier,
                question__in=question_pks
            )

            serializers = [
                AnswerSerializer(answer) for answer in user_poll_answers
            ]
            return Response([s.data for s in serializers])

        return Response(status=HTTP_200_OK)

    def get_serializer_class(self):
        if self.action == 'create':
            serializer_class = PollCreateSerializer
        else:
            serializer_class = PollDefaultSerializer

        return serializer_class

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = self.queryset

        query_params = self.request.query_params
        poll_pk = query_params.get('poll')

        if poll_pk:
            queryset = queryset.filter(poll=poll_pk)

        return queryset


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        queryset = self.queryset

        query_params = self.request.query_params
        question_pk = query_params.get('question')
        user_identifier = query_params.get('user_identifier')

        if question_pk:
            queryset = queryset.filter(question=question_pk)

        if user_identifier:
            queryset = queryset.filter(user_identifier=user_identifier)

        return queryset

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
