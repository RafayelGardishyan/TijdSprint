from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("boat_type", api.boat_typeViewSet)
router.register("race", api.raceViewSet)
router.register("crew", api.crewViewSet)
router.register("rower", api.rowerViewSet)
router.register("boat", api.boatViewSet)
router.register("heat", api.heatViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("participant_management/boat_type/", views.boat_typeListView.as_view(), name="participant_management_boat_type_list"),
    path("participant_management/boat_type/create/", views.boat_typeCreateView.as_view(), name="participant_management_boat_type_create"),
    path("participant_management/boat_type/detail/<int:pk>/", views.boat_typeDetailView.as_view(), name="participant_management_boat_type_detail"),
    path("participant_management/boat_type/update/<int:pk>/", views.boat_typeUpdateView.as_view(), name="participant_management_boat_type_update"),
    path("participant_management/boat_type/delete/<int:pk>/", views.boat_typeDeleteView.as_view(), name="participant_management_boat_type_delete"),
    path("participant_management/race/", views.raceListView.as_view(), name="participant_management_race_list"),
    path("participant_management/race/create/", views.raceCreateView.as_view(), name="participant_management_race_create"),
    path("participant_management/race/detail/<int:pk>/", views.raceDetailView.as_view(), name="participant_management_race_detail"),
    path("participant_management/race/update/<int:pk>/", views.raceUpdateView.as_view(), name="participant_management_race_update"),
    path("participant_management/race/delete/<int:pk>/", views.raceDeleteView.as_view(), name="participant_management_race_delete"),
    path("participant_management/crew/", views.crewListView.as_view(), name="participant_management_crew_list"),
    path("participant_management/crew/create/", views.crewCreateView.as_view(), name="participant_management_crew_create"),
    path("participant_management/crew/detail/<int:pk>/", views.crewDetailView.as_view(), name="participant_management_crew_detail"),
    path("participant_management/crew/update/<int:pk>/", views.crewUpdateView.as_view(), name="participant_management_crew_update"),
    path("participant_management/crew/delete/<int:pk>/", views.crewDeleteView.as_view(), name="participant_management_crew_delete"),
    path("participant_management/rower/", views.rowerListView.as_view(), name="participant_management_rower_list"),
    path("participant_management/rower/create/", views.rowerCreateView.as_view(), name="participant_management_rower_create"),
    path("participant_management/rower/detail/<slug:slug>/", views.rowerDetailView.as_view(), name="participant_management_rower_detail"),
    path("participant_management/rower/update/<slug:slug>/", views.rowerUpdateView.as_view(), name="participant_management_rower_update"),
    path("participant_management/rower/delete/<slug:slug>/", views.rowerDeleteView.as_view(), name="participant_management_rower_delete"),
    path("participant_management/boat/", views.boatListView.as_view(), name="participant_management_boat_list"),
    path("participant_management/boat/create/", views.boatCreateView.as_view(), name="participant_management_boat_create"),
    path("participant_management/boat/detail/<slug:slug>/", views.boatDetailView.as_view(), name="participant_management_boat_detail"),
    path("participant_management/boat/update/<slug:slug>/", views.boatUpdateView.as_view(), name="participant_management_boat_update"),
    path("participant_management/boat/delete/<slug:slug>/", views.boatDeleteView.as_view(), name="participant_management_boat_delete"),
    path("participant_management/heat/", views.heatListView.as_view(), name="participant_management_heat_list"),
    path("participant_management/heat/create/", views.heatCreateView.as_view(), name="participant_management_heat_create"),
    path("participant_management/heat/detail/<int:pk>/", views.heatDetailView.as_view(), name="participant_management_heat_detail"),
    path("participant_management/heat/update/<int:pk>/", views.heatUpdateView.as_view(), name="participant_management_heat_update"),
    path("participant_management/heat/delete/<int:pk>/", views.heatDeleteView.as_view(), name="participant_management_heat_delete"),
)
