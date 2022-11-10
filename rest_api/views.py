from django.shortcuts import render
from rest_framework import viewsets
from .models import Restaurant
from .serializers import RestaurantSerializer
from django.http import HttpResponse
from rest_framework.response import Response
import json
# Create your views here.

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def create(self, request, *args, **kwargs):
        return HttpResponse(json.dumps({
            'code': 201,
            'message':'restaurant added successfully'
        }), content_type='application/json')
        
