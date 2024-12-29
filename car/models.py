from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Cars', null=True, blank=True, )
    def __str__(self):
        return self.name


class Car(models.Model):
    image = models.ImageField(upload_to='Cars', null=False, blank=False)
    car_name = models.CharField(max_length=100)
    category = models.ForeignKey(category, on_delete=models.CASCADE,blank=True, null =True)
    company_name = models.CharField(max_length=100)
    num_of_seats = models.IntegerField()
    cost_par_day = models.IntegerField()
    description = models.TextField()
    is_available= models.BooleanField(default=True)
    like = models.IntegerField(default=0)
    
    

    def __str__(self):
        return self.car_name


from django.db import models
from datetime import date
from django.utils import timezone

class Booking(models.Model):
  customer = models.ForeignKey(User, on_delete=models.CASCADE)
  car = models.ForeignKey(Car, on_delete=models.CASCADE)
  rental_start_date = models.DateField()
  rental_end_date = models.DateField()
  pickup_location = models.CharField(max_length=255)
  dropoff_location = models.CharField(max_length=255)
  booked_at = models.DateTimeField(default=timezone.now)
  phone = models.CharField(max_length=11)
  # Adjust max_digits and decimal_places as needed

  def __str__(self):
        return f"{self.customer} - {self.car} (Booking ID: {self.id})"
  
  def save(self, *args, **kwargs):
        # Calculate and save the total price before saving the booking
        num_days = (self.rental_end_date - self.rental_start_date).days
        total_price = num_days * self.car.cost_par_day
        super().save(*args, **kwargs)
        


  
    
