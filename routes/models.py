from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from passengers.models import Passenger


@python_2_unicode_compatible
class Route(models.Model):
    departure = models.CharField(max_length=100, null=False, blank=False)
    arrival = models.CharField(max_length=100, null=False, blank=False)
    comments = models.CharField(max_length=200, null=True, blank=True)
    sits = models.IntegerField(default=1, null=False, blank=False)
    contact = models.ForeignKey('passengers.Passenger', related_name='%(class)s_contact', default=None)
    passengers = models.ManyToManyField(Passenger)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'routes'
        ordering = ['departure', 'arrival']
