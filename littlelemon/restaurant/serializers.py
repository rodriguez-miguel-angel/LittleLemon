from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User

from .models import Booking, Menu


"""
version-01:
"""
class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']


class BookingSerializer(ModelSerializer):    
    class Meta:
        model = Booking
        fields = "__all__"

