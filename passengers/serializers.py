from rest_framework import serializers
from .models import Passenger


class PassengerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ('pk',
                  'username',
                  'first_name',
                  'last_name')

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ('pk',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'skype_id',
                  'cellphone')