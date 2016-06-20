from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Route
from .serializers import RouteListSerializer, RouteSerializer
from passengers.models import Passenger


@api_view(['GET', ])
def route_list(request):
    """
        Returns a Routes list detail
    ---
    response_serializer: routes.serializers.RouteListSerializer
    responseMessages:
    - code: 400
      message: Bad request
    - code: 404
      message: Not found.
    """
    if request.method == 'GET':
        routes = Route.objects.all()
        serializer = RouteListSerializer(routes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def route_by_id(request, route_id):
    """
        Returns a Route detail by id
    ---
    response_serializer: routes.serializers.RouteSerializer
    responseMessages:
    - code: 400
      message: Bad request
    - code: 404
      message: Not found.
    """
    if request.method == 'GET':
        route = get_object_or_404(Route, pk=route_id)
        serializer = RouteSerializer(route)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def route_list_by_passenger(request, passenger_id):
    """
        Returns a Route list by Passenger
    ---
    response_serializer: routes.serializers.RouteSerializer
    responseMessages:
    - code: 400
      message: Bad request
    - code: 404
      message: Not found.
    """
    if request.method == 'GET':
        passenger = get_object_or_404(Passenger, pk=passenger_id)
        routes = Route.objects.filter(passenger=passenger)
        serializer = RouteSerializer(routes)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', ])
def route_add_new(request):
    """
        Add a new Route on database
    ---
    response_serializer: routes.serializers.RouteSerializer
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
        passengers = []
        departure_value = (request.data['departure'])
        arrival_value = (request.data['arrival'])
        comments_value = (request.data['comments'] if 'comments' in request.data.keys() else None)
        contact = get_object_or_404(Passenger, pk=request.data['contact'])
        passengers.append(contact.id)
        sits_value = (request.data['sits'] if 'sits' in request.data.keys() else 1)
        data = {"departure": departure_value,
                "arrival": arrival_value,
                "comments": comments_value,
                "sits": sits_value,
                "contact": contact.id,
                "passengers": passengers}
        serializer = RouteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            content = {'detail': 'Successful route added'}
            return Response(content, status=status.HTTP_201_CREATED)
        else:
            errors.append(serializer.errors)
            content = {'error': errors}
            return Response(content, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['UPDATE', ])
def route_update(request):
    pass
