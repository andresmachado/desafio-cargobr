from django.shortcuts import render
from rest_framework import viewsets

from .serializers import MapSerializer, RouteSerializer
from .models import Map, Route
# Create your views here.


class MapViewSet(viewsets.ModelViewSet):
    serializer_class = MapSerializer
    queryset = Map.objects.all()


class RoutesViewSet(viewsets.ModelViewSet):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()