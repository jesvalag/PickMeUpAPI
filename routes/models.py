from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from passengers.models import Passenger


@python_2_unicode_compatible
class Route(models.Model):
    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)
    comments = models.CharField(max_length=200, null=True, blank=True)
    passenger = models.ManyToManyField(Passenger)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'routes'
        ordering = ['departure', 'arrival']
