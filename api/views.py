"""API Views."""
from django.core import serializers
from django.db.models import Q, Min, Sum
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route

from .serializers import MapSerializer, RouteSerializer
from .models import Map, Route

# Create your views here.


class MapViewSet(viewsets.ModelViewSet):
    """Endpoint to add, remove and edit maps."""

    serializer_class = MapSerializer
    queryset = Map.objects.all()

    @detail_route(methods=['get'])
    def routes(self, request, pk=None):
        """Endpoint to calculate the best route given all parameters in request."""
        given_map = self.get_object()
        origin = request.query_params.get('origem', None)
        destiny = request.query_params.get('destino', None)
        autonomy = request.query_params.get('autonomia', None)
        lit_price = request.query_params.get('valor_litro', None)
        coord = list(origin + destiny)

        if origin and destiny and autonomy and lit_price:
            initial_route = given_map.routes.filter(origin=origin, destiny=destiny)

            if not initial_route.exists():
                initial_route = given_map.routes.filter(Q(origin__in=coord) | Q(destiny__in=coord))
                # initial_route = initial_route.exclude(~Q(origin__in=coord))
            response = initial_route.values('origin', 'destiny', 'distance').order_by('origin')
            # serializer = serializers.serialize('json', response)

            # kilometers = initial_route.aggregate(km=Sum('distance'))
            # kilometers = int(kilometers.get('km'))
            # dist_autonomy = kilometers / float(autonomy) * float(lit_price)

            serializer = list(response)
            # msg = '{}-{}-{}-{}'.format(origin, destiny, autonomy, lit_price)
            return Response(serializer)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RoutesViewSet(viewsets.ModelViewSet):
    """Endpoint to add, remove and edit routes."""

    serializer_class = RouteSerializer
    queryset = Route.objects.all()
