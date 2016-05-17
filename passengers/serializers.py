from rest_framework import serializers
from .models import Passenger


class PassengerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ('pk',
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'skype_id')