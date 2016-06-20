from django.test import TestCase
from passengers.models import Passenger
# Create your tests here.


def test_new_route():
    contact = Passenger()
    contact.username = "usertest"
    contact.first_name = "first_name"
    contact.last_name = "last_name"
    contact.skype_id = "skype_name"
    contact.cellphone = 98765432
    contact.save()
