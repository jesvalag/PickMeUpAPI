from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Passenger
from .serializers import PassengerListSerializer, PassengerSerializer


@api_view(['GET', ])
def passenger_list(request):
    if request.method == 'GET':
        passengers = Passenger.objects.all()
        serializer = PassengerListSerializer(passengers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def passenger_by_id(request, passenger_id):
    if request.method == 'GET':
        passenger = get_object_or_404(Passenger, pk=passenger_id)
        serializer = PassengerSerializer(passenger)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', ])
def passenger_add_new(request, passenger_id):
    pass


@api_view(['UPDATE', ])
def passenger_update(request, passenger_id):
    pass


def passenger_login(request):
    pass

def passenger_logout(request):
    pass