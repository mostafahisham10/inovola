from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import MachineSerializer, PodSerializer
from .models import Machine, Pod


class Index(TemplateView):
    template_name = "coffee/index.html"


# Overview for the rest api
class ApiOverview(APIView):

    def get(self, request):
        api_urls = {
            'Machine List': 'api/machine-list/',
            'Pod List': 'api/pod-detail/',
        }
        return Response(api_urls)


# Filter machines by all categories
class MachineList(ListAPIView):

    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("types", "model", "is_water")


# Filter pods by all categories
class PodList(ListAPIView):

    queryset = Pod.objects.all()
    serializer_class = PodSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("types", "flavor", "size")
