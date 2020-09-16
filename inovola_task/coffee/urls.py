from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/", views.apiOverview, name="api-overview"),
    path("api/machine-detail/<str:pk1>/<str:pk2>/<str:pk3>/", views.machineDetail, name="machine-detail"),
    path("api/machine-type/<str:pk>/", views.machineType, name="machine-type"),
    path("api/machine-model/<str:pk>/", views.machineModel, name="machine-model"),
    path("api/machine-water/<str:pk>/", views.machineWater, name="machine-water"),
    path("api/pod-detail/<str:pk1>/<str:pk2>/<str:pk3>/", views.podDetail, name="pod-detail"),
    path("api/pod-type/<str:pk>/", views.podType, name="pod-type"),
    path("api/pod-flavor/<str:pk>/", views.podFlavor, name="pod-flavor"),
    path("api/pod-size/<str:pk>/", views.podSize, name="pod-size"),
]
