from django import forms
from . import models


class resultForm(forms.ModelForm):
    class Meta:
        model = models.result
        fields = [
            "start_time",
            "finish_time",
            "heat",
            "crew",
        ]
