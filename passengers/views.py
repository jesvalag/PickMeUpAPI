from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Passenger
from .serializers import PassengerListSerializer


@api_view(['GET', ])
def passenger_list(request):
    if request.method == 'GET':
        passengers = Passenger.objects.all()
        serializer = PassengerListSerializer(passengers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
