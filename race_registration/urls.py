from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("result", api.resultViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("race_registration/result/", views.resultListView.as_view(), name="race_registration_result_list"),
    path("race_registration/result/create/", views.resultCreateView.as_view(), name="race_registration_result_create"),
    path("race_registration/result/detail/<int:pk>/", views.resultDetailView.as_view(), name="race_registration_result_detail"),
    path("race_registration/result/update/<int:pk>/", views.resultUpdateView.as_view(), name="race_registration_result_update"),
    path("race_registration/result/delete/<int:pk>/", views.resultDeleteView.as_view(), name="race_registration_result_delete"),
)
