from django.http import HttpResponse, JsonResponse
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
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html')

@csrf_exempt
def book(request):
    if request.method == 'GET':
        print("request [book]:",request.method)
        form = BookingForm()
        # return render(request, 'book.html', {'form': form})
    if request.method == 'POST':
        print("request [book]:",request.method)
        form = BookingForm(request.POST)
        # return render(request, 'book.html', {'form': form})
        # if form.is_valid():
        #     form.save()
    context = {
        'form':form
    }
    return render(request, 'book.html', context)

@csrf_exempt
def booking(request):
    
    if request.method == 'GET':
        print("request [bookings]:",request.method)
    if request.method == 'POST':
        print("request [bookings]:",request.method)
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
        menu_items = Menu.objects.all()
        list_of_menu_items = []
        for menu_item in menu_items:
            list_of_menu_items.append(menu_item)
        
        context = {
            "message":"200 - OK.",
            "menu_items": list_of_menu_items
        }

        return render(request, 'menu.html', context)


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

    def get(self, request, pk):
        if pk: 
            menu_item = Menu.objects.get(pk=pk) 
        else: 
            menu_item = "" 
        context = {
            "message":"200 - OK.",
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


"""
version-01:

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

"""



class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    """
    version-01 [insecure]:
    permission_classes = []
    version-02 [secure]:
    permission_classes = [IsAuthenticated]
    """
    permission_classes = []
    

    def get_permissions(self):
        if(self.request.method in ['GET', 'POST']):
            return []
        else:
            return [IsAuthenticated()]


    ordering_fields = ['name', 'booking_date']
    filterset_fields = ['name', 'booking_date']
    search_fields = ['booking_date']

    def list(self, request):
        date = request.GET.get('date',datetime.today().date())
        bookings = Booking.objects.all()
        booking_json = serializers.serialize('json', bookings)
        context = {
            "message": "200 - OK.",
            'date': date,
            'list': booking_json
        }
        return render(request, 'bookings.html',context)
    
    """
    See <https://www.django-rest-framework.org/api-guide/viewsets/>.
    Unsupported Media Type:
    """
    def create(self, request):
        """
        version-01:
        serializer = BookingSerializer(data=self.request.data)
        if serializer.is_valid():
            print("dos",serializer)
            # serializer.save()
            print(serializer.validated_data['name'])
            booking = Booking(
                name=serializer.validated_data['name'],
                booking_date=serializer.validated_data['booking_date'],
                no_of_guests=serializer.validated_data['no_of_guests'],
            )
            booking.save()
            return HttpResponse(booking, "HTTP_200_OK")
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
        """
        print("self...",self.action)
        print("create:", self.request)
        
        print("self...",request)
        print("method:", self.request.method)
        print("data:", self.request.data)
        serializer = BookingSerializer(data=self.request.data)
        
        print("serializer:", serializer)
        # form = BookingForm(data=self.request.data)
        # print("form: ",form)
        # data = json.load(self.request)
        # print("data:", data)
        # if form.is_valid():
        #     print("yup...")
            # cd = form.cleaned_data

        if serializer.is_valid():
            booking = Booking(
                name=serializer.validated_data['name'],
                booking_date=serializer.validated_data['booking_date'],
                no_of_guests=serializer.validated_data['no_of_guests'],
            )
            booking.save()
            return HttpResponse(booking, "HTTP_2001_CREATED")
        else:
            return HttpResponse("{'message':'HTTP_400_BAD_REQUEST'}", content_type='application/json')
            
        
        # book(request)
"""
    date = request.GET.get('date',datetime.today().date())
    print("date",date)
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    context = {
        'date':date,
        'bookings': booking_json
        }
    return render(request, 'bookings.html',context)

"""



class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 