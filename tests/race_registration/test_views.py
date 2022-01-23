import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_result_list_view():
    instance1 = test_helpers.create_race_registration_result()
    instance2 = test_helpers.create_race_registration_result()
    client = Client()
    url = reverse("race_registration_result_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_result_create_view():
    heat = test_helpers.create_participant_management_heat()
    crew = test_helpers.create_participant_management_crew()
    client = Client()
    url = reverse("race_registration_result_create")
    data = {
        "start_time": datetime.now(),
        "finish_time": datetime.now(),
        "heat": heat.pk,
        "crew": crew.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_result_detail_view():
    client = Client()
    instance = test_helpers.create_race_registration_result()
    url = reverse("race_registration_result_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_result_update_view():
    heat = test_helpers.create_participant_management_heat()
    crew = test_helpers.create_participant_management_crew()
    client = Client()
    instance = test_helpers.create_race_registration_result()
    url = reverse("race_registration_result_update", args=[instance.pk, ])
    data = {
        "start_time": datetime.now(),
        "finish_time": datetime.now(),
        "heat": heat.pk,
        "crew": crew.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
