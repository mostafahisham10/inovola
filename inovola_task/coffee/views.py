from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MachineSerializer, PodSerializer
from .models import Machine, Pod


def index(request):
    return render(request, "coffee/index.html")


# Overview for the rest api
class ApiOverview(APIView):

    def get(self, request):
        api_urls = {
            'Machine Detail': 'api/machine-detail/<str:pk1>/<str:pk2>/<str:pk3>/',
            'Machine Type': 'api/machine-type/<str:pk>/',
            'Machine Model': 'api/machine-model/<str:pk>/',
            'Machine Water': 'api/machine-water/<str:pk>/',
            'Pod Detail': 'api/pod-detail/<str:pk1>/<str:pk2>/<str:pk3>/',
            'Pod Type': 'api/pod-type/<str:pk>/',
            'Pod Flavor': 'api/pod-flavor/<str:pk>/',
            'Pod Size': 'api/pod-size/<str:pk>/',
        }
        return Response(api_urls)


# Filter machines by all categories
class MachineDetail(APIView):

    def get(self, request, pk1, pk2, pk3):
        machines = Machine.objects.filter(types=pk1, model=pk2, is_water=pk3)
        serializer = MachineSerializer(machines, many=True)
        return Response(serializer.data)


# Filter machines by product type
class MachineType(APIView):

    def get(self, request, pk):
        machines = Machine.objects.filter(types=pk)
        serializer = MachineSerializer(machines, many=True)
        return Response(serializer.data)


# Filter machines by model
class MachineModel(APIView):

    def get(self,request, pk):
        machines = Machine.objects.filter(model=pk)
        serializer = MachineSerializer(machines, many=True)
        return Response(serializer.data)


# Filter machines by water line compatibility
class MachineWater(APIView):

    def get(self, request, pk):
        machines = Machine.objects.filter(is_water=pk)
        serializer = MachineSerializer(machines, many=True)
        return Response(serializer.data)


# Filter pods by all categories
class PodDetail(APIView):

    def get(self, request, pk1, pk2, pk3):
        pods = Pod.objects.filter(types=pk1, flavor=pk2, size=pk3)
        serializer = PodSerializer(pods, many=True)
        return Response(serializer.data)


# Filter pods by product type
class PodType(APIView):

    def get(self, request, pk):
        pods = Pod.objects.filter(types=pk)
        serializer = PodSerializer(pods, many=True)
        return Response(serializer.data)


# Filter pods by flavor
class PodFlavor(APIView):

    def get(self, request, pk):
        pods = Pod.objects.filter(flavor=pk)
        serializer = PodSerializer(pods, many=True)
        return Response(serializer.data)


# Filter pods by size
class PodSize(APIView):
    def get(self, request, pk):
        pods = Pod.objects.filter(size=pk)
        serializer = PodSerializer(pods, many=True)
        return Response(serializer.data)
