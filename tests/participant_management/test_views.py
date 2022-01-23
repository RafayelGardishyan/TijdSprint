import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_boat_type_list_view():
    instance1 = test_helpers.create_participant_management_boat_type()
    instance2 = test_helpers.create_participant_management_boat_type()
    client = Client()
    url = reverse("participant_management_boat_type_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_boat_type_create_view():
    client = Client()
    url = reverse("participant_management_boat_type_create")
    data = {
        "correction": 1.0f,
        "code": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_boat_type_detail_view():
    client = Client()
    instance = test_helpers.create_participant_management_boat_type()
    url = reverse("participant_management_boat_type_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_boat_type_update_view():
    client = Client()
    instance = test_helpers.create_participant_management_boat_type()
    url = reverse("participant_management_boat_type_update", args=[instance.pk, ])
    data = {
        "correction": 1.0f,
        "code": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_race_list_view():
    instance1 = test_helpers.create_participant_management_race()
    instance2 = test_helpers.create_participant_management_race()
    client = Client()
    url = reverse("participant_management_race_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_race_create_view():
    client = Client()
    url = reverse("participant_management_race_create")
    data = {
        "end_date": datetime.now(),
        "description": "text",
        "start_date": datetime.now(),
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_race_detail_view():
    client = Client()
    instance = test_helpers.create_participant_management_race()
    url = reverse("participant_management_race_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_race_update_view():
    client = Client()
    instance = test_helpers.create_participant_management_race()
    url = reverse("participant_management_race_update", args=[instance.pk, ])
    data = {
        "end_date": datetime.now(),
        "description": "text",
        "start_date": datetime.now(),
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_crew_list_view():
    instance1 = test_helpers.create_participant_management_crew()
    instance2 = test_helpers.create_participant_management_crew()
    client = Client()
    url = reverse("participant_management_crew_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_crew_create_view():
    rowers = test_helpers.create_participant_management_rower()
    boat = test_helpers.create_participant_management_boat()
    client = Client()
    url = reverse("participant_management_crew_create")
    data = {
        "name": "text",
        "rowers": rowers.pk,
        "boat": boat.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_crew_detail_view():
    client = Client()
    instance = test_helpers.create_participant_management_crew()
    url = reverse("participant_management_crew_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_crew_update_view():
    rowers = test_helpers.create_participant_management_rower()
    boat = test_helpers.create_participant_management_boat()
    client = Client()
    instance = test_helpers.create_participant_management_crew()
    url = reverse("participant_management_crew_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "rowers": rowers.pk,
        "boat": boat.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_rower_list_view():
    instance1 = test_helpers.create_participant_management_rower()
    instance2 = test_helpers.create_participant_management_rower()
    client = Client()
    url = reverse("participant_management_rower_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_rower_create_view():
    client = Client()
    url = reverse("participant_management_rower_create")
    data = {
        "gender": "text",
        "slug": "slug",
        "full_name": "text",
        "date_of_birth": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_rower_detail_view():
    client = Client()
    instance = test_helpers.create_participant_management_rower()
    url = reverse("participant_management_rower_detail", args=[instance.slug, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_rower_update_view():
    client = Client()
    instance = test_helpers.create_participant_management_rower()
    url = reverse("participant_management_rower_update", args=[instance.slug, ])
    data = {
        "gender": "text",
        "slug": "slug",
        "full_name": "text",
        "date_of_birth": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_boat_list_view():
    instance1 = test_helpers.create_participant_management_boat()
    instance2 = test_helpers.create_participant_management_boat()
    client = Client()
    url = reverse("participant_management_boat_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_boat_create_view():
    boat_type = test_helpers.create_participant_management_boat_type()
    client = Client()
    url = reverse("participant_management_boat_create")
    data = {
        "name": "text",
        "slug": "slug",
        "boat_type": boat_type.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_boat_detail_view():
    client = Client()
    instance = test_helpers.create_participant_management_boat()
    url = reverse("participant_management_boat_detail", args=[instance.slug, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_boat_update_view():
    boat_type = test_helpers.create_participant_management_boat_type()
    client = Client()
    instance = test_helpers.create_participant_management_boat()
    url = reverse("participant_management_boat_update", args=[instance.slug, ])
    data = {
        "name": "text",
        "slug": "slug",
        "boat_type": boat_type.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_heat_list_view():
    instance1 = test_helpers.create_participant_management_heat()
    instance2 = test_helpers.create_participant_management_heat()
    client = Client()
    url = reverse("participant_management_heat_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_heat_create_view():
    crews = test_helpers.create_participant_management_crew()
    race = test_helpers.create_participant_management_race()
    client = Client()
    url = reverse("participant_management_heat_create")
    data = {
        "name": "text",
        "distance": 1,
        "start_time": datetime.now(),
        "crews": crews.pk,
        "race": race.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_heat_detail_view():
    client = Client()
    instance = test_helpers.create_participant_management_heat()
    url = reverse("participant_management_heat_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_heat_update_view():
    crews = test_helpers.create_participant_management_crew()
    race = test_helpers.create_participant_management_race()
    client = Client()
    instance = test_helpers.create_participant_management_heat()
    url = reverse("participant_management_heat_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "distance": 1,
        "start_time": datetime.now(),
        "crews": crews.pk,
        "race": race.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
