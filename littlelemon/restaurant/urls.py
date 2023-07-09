from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('menu', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu_item'),
    # version-01:
    # path('reservations/', views.reservations, name="reservations"),
    path('reservations/', views.BookingViewSet.as_view({'get':'list'}), name='reservations'), 
    
    # version-01:
    # path('book/', views.book, name="book"),
    # path('bookings', views.bookings, name='bookings'),
    path('book', views.book, name="book"),
    path('booking', views.booking, name='booking'),
    path('bookings', views.BookingViewSet.as_view({'post':'create'}), name="bookings"),
    path('api-token-auth/', obtain_auth_token),
]