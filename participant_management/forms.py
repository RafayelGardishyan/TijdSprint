from django import forms
from . import models


class boat_typeForm(forms.ModelForm):
    class Meta:
        model = models.boat_type
        fields = [
            "correction",
            "code",
        ]


class raceForm(forms.ModelForm):
    class Meta:
        model = models.race
        fields = [
            "end_date",
            "description",
            "start_date",
            "name",
        ]


class crewForm(forms.ModelForm):
    class Meta:
        model = models.crew
        fields = [
            "name",
            "rowers",
            "boat",
        ]


class rowerForm(forms.ModelForm):
    class Meta:
        model = models.rower
        fields = [
            "gender",
            "slug",
            "full_name",
            "date_of_birth",
        ]


class boatForm(forms.ModelForm):
    class Meta:
        model = models.boat
        fields = [
            "name",
            "slug",
            "boat_type",
        ]


class heatForm(forms.ModelForm):
    class Meta:
        model = models.heat
        fields = [
            "name",
            "distance",
            "start_time",
            "crews",
            "race",
        ]
