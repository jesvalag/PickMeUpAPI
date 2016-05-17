from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Passenger(AbstractUser):
    skype_id = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['first_name', 'last_name', 'username']
