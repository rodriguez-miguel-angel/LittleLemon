from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu_item'),
    path('bookings', views.bookings, name='bookings'), 
    path('api-token-auth/', obtain_auth_token),
]