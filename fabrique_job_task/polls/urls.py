from django.urls import path, include

from rest_framework import routers

from .views import PollViewSet, QuestionViewSet, AnswerViewSet


router = routers.DefaultRouter()

router.register(r'poll', viewset=PollViewSet)
router.register(r'question', viewset=QuestionViewSet)
router.register(r'answer', viewset=AnswerViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
