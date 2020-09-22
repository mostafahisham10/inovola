from django.urls import path
from .views import (
    Index,
    ApiOverview,
    MachineList,
    PodList,
)


urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("api/", ApiOverview.as_view(), name="api-overview"),
    path("api/machine-list/", MachineList.as_view(), name="machine-list"),
    path("api/pod-list/", PodList.as_view(), name="pod-detail"),
]
