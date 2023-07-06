from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView

from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from .forms import BookingForm

from .models import Booking, Menu
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer
from django.core import serializers

from datetime import datetime

import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html')

def book(request):
    print("request [book]:",request)
    if request.method == 'GET':
        form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form':form
        }
    print("form", form)
    return render(request, 'book.html', context)

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        print(data)
        exist = Booking.objects.filter(booking_date=data['booking_date']).filter(
            name=data['name']).exists()
        if exist==False:
            booking = Booking(
                name=data['name'],
                booking_date=data['booking_date'],
                no_of_guests=data['no_of_guests'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
        
    date = request.GET.get('date',datetime.today().date())

    bookings = Booking.objects.all().filter(booking_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')


def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    print("date",date)
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    context = {
        'date':date,
        'bookings': booking_json
        }
    return render(request, 'bookings.html',context)

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    """
    version-01 [insecure]:
    permission_classes = []
    version-02 [secure]:
    permission_classes = [IsAuthenticated]
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        menu_data = Menu.objects.all()
        main_data = {"menu": menu_data}
        return render(request, 'menu.html', {"menu": main_data})
        


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

    def get(self, request, pk):
        if pk: 
            menu_item = Menu.objects.get(pk=pk) 
        else: 
            menu_item = "" 
        context = {
            "menu_item": menu_item
        }  
        return render(request, 'menu_item.html', context) 

    def put(self, request, pk):
        payload = self.request.data
        modified_menu_item = Menu.objects.get(pk=pk)
        modified_menu_item.title = payload['title']
        modified_menu_item.price = payload['price']
        modified_menu_item.inventory = payload['inventory']
        modified_menu_item.save()
        context = {
            "message":"200 - Success.",
            "status": "HTTP_200_OK",
        }
        return render(request, 'bookings.html',context)



class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    """
    version-01 [insecure]:
    permission_classes = []
    version-02 [secure]:
    permission_classes = [IsAuthenticated]
    """
    permission_classes = [IsAuthenticated]

    ordering_fields = ['name', 'booking_date']
    filterset_fields = ['name', 'booking_date']
    search_fields = ['booking_date']


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 