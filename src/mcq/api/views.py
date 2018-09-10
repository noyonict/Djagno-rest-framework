from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics, mixins
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import QuestionSerializer, ChoiceSerializer
from mcq.models import Question, Choice


# Model View sets and routers
class ChoiceModelViewSets(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    lookup_field = 'id'


class QuestionModelViewSets(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
