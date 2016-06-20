from rest_framework import serializers
from .models import Route


class RouteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        depth = 1
        fields = ('pk',
                  'departure',
                  'arrival',
                  'sits',
                  'contact')


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('pk',
                  'departure',
                  'arrival',
                  'comments',
                  'sits',
                  'contact',
                  'passengers')