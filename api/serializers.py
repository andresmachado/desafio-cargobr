from rest_framework import serializers

from .models import Map, Route


class RouteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Route
        fields = ('origin', 'destiny', 'distance')

class MapSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True)
    
    class Meta:
        model = Map
        fields = ('name', 'routes')


