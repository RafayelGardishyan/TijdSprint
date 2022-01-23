from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class resultListView(generic.ListView):
    model = models.result
    form_class = forms.resultForm


class resultCreateView(generic.CreateView):
    model = models.result
    form_class = forms.resultForm


class resultDetailView(generic.DetailView):
    model = models.result
    form_class = forms.resultForm


class resultUpdateView(generic.UpdateView):
    model = models.result
    form_class = forms.resultForm
    pk_url_kwarg = "pk"


class resultDeleteView(generic.DeleteView):
    model = models.result
    success_url = reverse_lazy("race_registration_result_list")
