from rest_framework import status
from rest_framework.test import APITestCase
from .models import Passenger
from .serializers import PassengerListSerializer
from django.core.urlresolvers import reverse


class PassengerTestCase(APITestCase):
    def setUp(self):
        Passenger.objects.create_superuser('user1', 'user1@email.com', 'password1')
        Passenger.objects.create_superuser('user2', 'user2@email.com', 'password2')

    def test_passenger_list(self):
        passengers = Passenger.objects.all()
        response_data = PassengerListSerializer(passengers, many=True).data
        url = reverse('passengers:passenger_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.data, response_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)