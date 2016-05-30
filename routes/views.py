from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Route
from .serializers import RouteListSerializer, RouteSerializer
from passengers.models import Passenger


@api_view(['GET', ])
def route_list(request):
    if request.method == 'GET':
        routes = Route.objects.all()
        serializer = RouteListSerializer(routes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def route_by_id(request, route_id):
    if request.method == 'GET':
        route = get_object_or_404(Route, pk=route_id)
        serializer = RouteSerializer(route)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def route_list_by_passenger(request, passenger_id):
    if request.method == 'GET':
        passenger = get_object_or_404(Passenger, pk=passenger_id)
        routes = Route.objects.filter(passenger=passenger)
        serializer = RouteSerializer(routes)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', ])
def route_add_new(request):
    pass


@api_view(['UPDATE', ])
def route_update(request):
    pass
