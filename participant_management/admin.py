from django.contrib import admin
from django import forms

from . import models


class boat_typeAdminForm(forms.ModelForm):

    class Meta:
        model = models.boat_type
        fields = "__all__"


class boat_typeAdmin(admin.ModelAdmin):
    form = boat_typeAdminForm
    list_display = [
        "code",
        "correction",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class raceAdminForm(forms.ModelForm):

    class Meta:
        model = models.race
        fields = "__all__"


class raceAdmin(admin.ModelAdmin):
    form = raceAdminForm
    list_display = [
        "name",
        "start_date",
        "end_date",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "slug",
    ]


class crewAdminForm(forms.ModelForm):

    class Meta:
        model = models.crew
        fields = "__all__"


class crewAdmin(admin.ModelAdmin):
    form = crewAdminForm
    list_display = [
        "name",
        "boat",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "slug",
    ]


class rowerAdminForm(forms.ModelForm):

    class Meta:
        model = models.rower
        fields = "__all__"


class rowerAdmin(admin.ModelAdmin):
    form = rowerAdminForm
    list_display = [
        "full_name",
        "gender",
        "date_of_birth",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "slug",
    ]


class boatAdminForm(forms.ModelForm):

    class Meta:
        model = models.boat
        fields = "__all__"


class boatAdmin(admin.ModelAdmin):
    form = boatAdminForm
    list_display = [
        "name",
        "boat_type"
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "slug",
    ]


class heatAdminForm(forms.ModelForm):

    class Meta:
        model = models.heat
        fields = "__all__"


class heatAdmin(admin.ModelAdmin):
    form = heatAdminForm
    list_display = [
        "name",
        "distance",
        "start_time",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "slug",
    ]


admin.site.register(models.boat_type, boat_typeAdmin)
admin.site.register(models.race, raceAdmin)
admin.site.register(models.crew, crewAdmin)
admin.site.register(models.rower, rowerAdmin)
admin.site.register(models.boat, boatAdmin)
admin.site.register(models.heat, heatAdmin)
