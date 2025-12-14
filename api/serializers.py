from rest_framework import serializers
from .models import MissionObjective

class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionObjective
        fields = '__all__'