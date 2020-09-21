from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/", views.ApiOverview.as_view(), name="api-overview"),
    path("api/machine-detail/<str:pk1>-<str:pk2>-<str:pk3>/", views.MachineDetail.as_view(), name="machine-detail"),
    path("api/machine-type/<str:pk>/", views.MachineType.as_view(), name="machine-type"),
    path("api/machine-model/<str:pk>/", views.MachineModel.as_view(), name="machine-model"),
    path("api/machine-water/<str:pk>/", views.MachineWater.as_view(), name="machine-water"),
    path("api/pod-detail/<str:pk1>-<str:pk2>-<str:pk3>/", views.PodDetail.as_view(), name="pod-detail"),
    path("api/pod-type/<str:pk>/", views.PodType.as_view(), name="pod-type"),
    path("api/pod-flavor/<str:pk>/", views.PodFlavor.as_view(), name="pod-flavor"),
    path("api/pod-size/<str:pk>/", views.PodSize.as_view(), name="pod-size"),
]
