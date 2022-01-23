from django.contrib import admin
from django import forms

from . import models


class resultAdminForm(forms.ModelForm):

    class Meta:
        model = models.result
        fields = "__all__"


class resultAdmin(admin.ModelAdmin):
    form = resultAdminForm
    list_display = [
        "created",
        "last_updated",
        "start_time",
        "finish_time",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "start_time",
        "finish_time",
    ]


admin.site.register(models.result, resultAdmin)
