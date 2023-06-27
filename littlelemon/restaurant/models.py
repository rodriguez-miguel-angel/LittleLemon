from django.db import models

# Create your models here.
# Booking model
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveSmallIntegerField(default=0)
    booking_date = models.DateField()
    
    def __str__(self): 
        return f"[[Booking]] name: {self.name}. no_of_guests: {self.no_of_guests}. booking_date: {self.booking_date}."


# Menu model
class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=10, decimal_places=2) 
   inventory = models.PositiveSmallIntegerField(default=0)

   def __str__(self):
      return f"[[Menu]] title: {self.title}. price: {self.price}. inventory: {self.inventory}."
   
   