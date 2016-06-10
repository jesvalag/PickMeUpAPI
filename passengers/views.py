from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Passenger
from .serializers import PassengerListSerializer, PassengerSerializer


@api_view(['GET', ])
def passenger_list(request):
    """
        Returns a Passengers list detail
    ---
    response_serializer: passengers.serializers.PassengerListSerializer
    responseMessages:
    - code: 400
      message: Bad request
    - code: 404
      message: Not found.
    """
    if request.method == 'GET':
        passengers = Passenger.objects.all()
        serializer = PassengerListSerializer(passengers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def passenger_by_id(request, passenger_id):
    """
        Returns a Passenger detail by id
    ---
    response_serializer: passengers.serializers.PassengerSerializer
    responseMessages:
    - code: 400
      message: Bad request
    - code: 404
      message: Not found.
    """
    if request.method == 'GET':
        passenger = get_object_or_404(Passenger, pk=passenger_id)
        serializer = PassengerSerializer(passenger)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', ])
def passenger_add_new(request):
    """
        Add a new Passenger on database
    ---
    response_serializer: passengers.serializers.PassengerSerializer
    responseMessages:
    - code: 400
      message: Bad request
    - code: 404
      message: Not found.
    parameters:
    - name: body
      required: true
      paramType: body
    """
    if request.method == 'POST':
        errors = []
        serializer = PassengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = {'detail': 'Successful passenger added'}
            return Response(content, status=status.HTTP_201_CREATED)
        else:
            errors.append(serializer.errors)
            content = {'error': errors}
            return Response(content, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['UPDATE', ])
def passenger_update(request, passenger_id):
    pass


def passenger_login(request):
    pass


def passenger_logout(request):
    pass