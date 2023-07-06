from django.forms import ModelForm

from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        """
        version-01:
        fields = "__all__"

        version-02:
        """
        fields = ('id','name', 'no_of_guests', 'booking_date')
