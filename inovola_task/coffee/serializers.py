from rest_framework import serializers
from .models import Machine, Pod


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ("title",)


class PodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pod
        fields = ("title",)
