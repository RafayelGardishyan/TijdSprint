import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from participant_management import models as participant_management_models
from race_registration import models as race_registration_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_participant_management_boat_type(**kwargs):
    defaults = {}
    defaults["correction"] = ""
    defaults["code"] = ""
    defaults.update(**kwargs)
    return participant_management_models.boat_type.objects.create(**defaults)
def create_participant_management_race(**kwargs):
    defaults = {}
    defaults["end_date"] = datetime.now()
    defaults["description"] = ""
    defaults["start_date"] = datetime.now()
    defaults["name"] = ""
    defaults.update(**kwargs)
    return participant_management_models.race.objects.create(**defaults)
def create_participant_management_crew(**kwargs):
    defaults = {}
    defaults["name"] = ""
    if "rowers" not in kwargs:
        defaults["rowers"] = create_participant_management_rower()
    if "boat" not in kwargs:
        defaults["boat"] = create_participant_management_boat()
    defaults.update(**kwargs)
    return participant_management_models.crew.objects.create(**defaults)
def create_participant_management_rower(**kwargs):
    defaults = {}
    defaults["gender"] = ""
    defaults["slug"] = ""
    defaults["full_name"] = ""
    defaults["date_of_birth"] = datetime.now()
    defaults.update(**kwargs)
    return participant_management_models.rower.objects.create(**defaults)
def create_participant_management_boat(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["slug"] = ""
    if "boat_type" not in kwargs:
        defaults["boat_type"] = create_participant_management_boat_type()
    defaults.update(**kwargs)
    return participant_management_models.boat.objects.create(**defaults)
def create_participant_management_heat(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["distance"] = ""
    defaults["start_time"] = datetime.now()
    if "crews" not in kwargs:
        defaults["crews"] = create_participant_management_crew()
    if "race" not in kwargs:
        defaults["race"] = create_participant_management_race()
    defaults.update(**kwargs)
    return participant_management_models.heat.objects.create(**defaults)
def create_race_registration_result(**kwargs):
    defaults = {}
    defaults["start_time"] = datetime.now()
    defaults["finish_time"] = datetime.now()
    if "heat" not in kwargs:
        defaults["heat"] = create_participant_management_heat()
    if "crew" not in kwargs:
        defaults["crew"] = create_participant_management_crew()
    defaults.update(**kwargs)
    return race_registration_models.result.objects.create(**defaults)
