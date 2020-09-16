from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MachineSerializer, PodSerializer
from .models import Machine, Pod

# Create your views here.


def index(request):
    return render(request, "coffee/index.html")


@api_view(["GET"])
def apiOverview(request):
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


@api_view(['GET'])
def machineDetail(request, pk1, pk2, pk3):
    machines = Machine.objects.filter(types=pk1, model=pk2, is_water=pk3)
    serializer = MachineSerializer(machines, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def machineType(request, pk):
    machines = Machine.objects.filter(types=pk)
    serializer = MachineSerializer(machines, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def machineModel(request, pk):
    machines = Machine.objects.filter(model=pk)
    serializer = MachineSerializer(machines, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def machineWater(request, pk):
    machines = Machine.objects.filter(is_water=pk)
    serializer = MachineSerializer(machines, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def podDetail(request, pk1, pk2, pk3):
    pods = Pod.objects.filter(types=pk1, flavor=pk2, size=pk3)
    serializer = PodSerializer(pods, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def podType(request, pk):
    pods = Pod.objects.filter(types=pk)
    serializer = PodSerializer(pods, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def podFlavor(request, pk):
    pods = Pod.objects.filter(flavor=pk)
    serializer = PodSerializer(pods, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def podSize(request, pk):
    pods = Pod.objects.filter(size=pk)
    serializer = PodSerializer(pods, many=True)
    return Response(serializer.data)
