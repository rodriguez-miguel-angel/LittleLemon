from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView

from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from .models import Booking, Menu
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 