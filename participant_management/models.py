from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class boat_type(models.Model):

    # Fields
    correction = models.FloatField()
    code = models.CharField(max_length=3)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.code)

    def get_absolute_url(self):
        return reverse("participant_management_boat_type_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("participant_management_boat_type_update", args=(self.pk,))


class race(models.Model):

    # Fields
    end_date = models.DateField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=1000)
    start_date = models.DateField()
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField()

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("participant_management_race_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("participant_management_race_update", args=(self.pk,))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + self.datetime.now().strftime("%m/%d/%Y"))
        super(race, self).save(*args, **kwargs)

class crew(models.Model):

    # Relationships
    rowers = models.ManyToManyField("participant_management.rower")
    boat = models.ForeignKey("participant_management.boat", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField()

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("participant_management_crew_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("participant_management_crew_update", args=(self.pk,))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + self.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        super(crew, self).save(*args, **kwargs)


class rower(models.Model):

    # Fields
    gender = models.CharField(max_length=1, choices=(("f",  "Female"), ("m",  "Male")), default="f")
    slug = models.SlugField()
    full_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    date_of_birth = models.DateField()

    class Meta:
        pass

    def __str__(self):
        return str(self.full_name)

    def get_absolute_url(self):
        return reverse("participant_management_rower_detail", args=(self.slug,))

    def get_update_url(self):
        return reverse("participant_management_rower_update", args=(self.slug,))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.full_name + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        super(rower, self).save(*args, **kwargs)


class boat(models.Model):

    # Relationships
    boat_type = models.ForeignKey("participant_management.boat_type", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        pass

    def __str__(self):
        return str("{} | {}".format(self.name, self.boat_type))

    def get_absolute_url(self):
        return reverse("participant_management_boat_detail", args=(self.slug,))

    def get_update_url(self):
        return reverse("participant_management_boat_update", args=(self.slug,))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(boat, self).save(*args, **kwargs)


class heat(models.Model):

    # Relationships
    crews = models.ManyToManyField("participant_management.crew")
    race = models.ForeignKey("participant_management.race", on_delete=models.CASCADE)

    # Fields
    name = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    distance = models.IntegerField(verbose_name="Distance (m)")
    start_time = models.DateTimeField()
    slug = models.SlugField()

    class Meta:
        pass

    def __str__(self):
        return str(self.race, self.name)

    def get_absolute_url(self):
        return reverse("participant_management_heat_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("participant_management_heat_update", args=(self.pk,))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        super(heat, self).save(*args, **kwargs)
