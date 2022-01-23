from django.db import models
from django.urls import reverse


class result(models.Model):

    # Relationships
    heat = models.ForeignKey("participant_management.heat", on_delete=models.CASCADE)
    crew = models.ForeignKey("participant_management.crew", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("race_registration_result_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("race_registration_result_update", args=(self.pk,))
