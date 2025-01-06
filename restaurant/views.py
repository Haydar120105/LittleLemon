from django.shortcuts import render
from .models import Booking, Menu

from .serializers import BookingSerializer, MenuSerializer

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class MenuItemview(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer(many=True)

class SingleMenuItemview(generics.RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer