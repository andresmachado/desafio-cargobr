from rest_framework import serializers

from .models import Map, Route


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('map_name', 'origin', 'destiny', 'distance')

class MapSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True, read_only=True)
    
    class Meta:
        model = Map
        fields = ('id', 'name', 'routes')


