from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class boat_typeListView(generic.ListView):
    model = models.boat_type
    form_class = forms.boat_typeForm


class boat_typeCreateView(generic.CreateView):
    model = models.boat_type
    form_class = forms.boat_typeForm


class boat_typeDetailView(generic.DetailView):
    model = models.boat_type
    form_class = forms.boat_typeForm


class boat_typeUpdateView(generic.UpdateView):
    model = models.boat_type
    form_class = forms.boat_typeForm
    pk_url_kwarg = "pk"


class boat_typeDeleteView(generic.DeleteView):
    model = models.boat_type
    success_url = reverse_lazy("participant_management_boat_type_list")


class raceListView(generic.ListView):
    model = models.race
    form_class = forms.raceForm


class raceCreateView(generic.CreateView):
    model = models.race
    form_class = forms.raceForm


class raceDetailView(generic.DetailView):
    model = models.race
    form_class = forms.raceForm


class raceUpdateView(generic.UpdateView):
    model = models.race
    form_class = forms.raceForm
    pk_url_kwarg = "pk"


class raceDeleteView(generic.DeleteView):
    model = models.race
    success_url = reverse_lazy("participant_management_race_list")


class crewListView(generic.ListView):
    model = models.crew
    form_class = forms.crewForm


class crewCreateView(generic.CreateView):
    model = models.crew
    form_class = forms.crewForm


class crewDetailView(generic.DetailView):
    model = models.crew
    form_class = forms.crewForm


class crewUpdateView(generic.UpdateView):
    model = models.crew
    form_class = forms.crewForm
    pk_url_kwarg = "pk"


class crewDeleteView(generic.DeleteView):
    model = models.crew
    success_url = reverse_lazy("participant_management_crew_list")


class rowerListView(generic.ListView):
    model = models.rower
    form_class = forms.rowerForm


class rowerCreateView(generic.CreateView):
    model = models.rower
    form_class = forms.rowerForm


class rowerDetailView(generic.DetailView):
    model = models.rower
    form_class = forms.rowerForm
    slug_url_kwarg = "slug"


class rowerUpdateView(generic.UpdateView):
    model = models.rower
    form_class = forms.rowerForm
    slug_url_kwarg = "slug"


class rowerDeleteView(generic.DeleteView):
    model = models.rower
    success_url = reverse_lazy("participant_management_rower_list")


class boatListView(generic.ListView):
    model = models.boat
    form_class = forms.boatForm


class boatCreateView(generic.CreateView):
    model = models.boat
    form_class = forms.boatForm


class boatDetailView(generic.DetailView):
    model = models.boat
    form_class = forms.boatForm
    slug_url_kwarg = "slug"


class boatUpdateView(generic.UpdateView):
    model = models.boat
    form_class = forms.boatForm
    slug_url_kwarg = "slug"


class boatDeleteView(generic.DeleteView):
    model = models.boat
    success_url = reverse_lazy("participant_management_boat_list")


class heatListView(generic.ListView):
    model = models.heat
    form_class = forms.heatForm


class heatCreateView(generic.CreateView):
    model = models.heat
    form_class = forms.heatForm


class heatDetailView(generic.DetailView):
    model = models.heat
    form_class = forms.heatForm


class heatUpdateView(generic.UpdateView):
    model = models.heat
    form_class = forms.heatForm
    pk_url_kwarg = "pk"


class heatDeleteView(generic.DeleteView):
    model = models.heat
    success_url = reverse_lazy("participant_management_heat_list")
