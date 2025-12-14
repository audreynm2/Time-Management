from django.shortcuts import render

from rest_framework import viewsets
from .models import MissionObjective
from .serializers import ObjectiveSerializer

class ObjectiveViewSet(viewsets.ModelViewSet):
    (retrieving all objectives)
    queryset = MissionObjective.objects.all().order_by('id') 

    serializer_class = ObjectiveSerializer
