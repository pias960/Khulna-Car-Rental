from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
  class Meta:
    model = Booking
    fields = ['rental_start_date', 'rental_end_date', 'pickup_location', 'dropoff_location']
    widget =  {
      'rental_start_date': forms.DateInput(attrs={'class': 'form-control' , 'type':'date', 'placeholder' :'YYYY-MM-DD'}),
      'rental_end_date': forms.DateInput(attrs={'class': 'form-control', 'type':'date', 'placeholder' :'YYYY-MM-DD'}),
      'pickup_location': forms.TextInput(attrs={'class': 'form-control'}),
      'dropoff_location': forms.TextInput(attrs={'class': 'form-control'}),
       
    }

  def clean(self):
    cleaned_data = super().clean()
    rental_start_date = cleaned_data.get('rental_start_date')
    rental_end_date = cleaned_data.get('rental_end_date')

    # Basic validation for booking dates (optional)
    if rental_start_date and rental_end_date:
      if rental_start_date >= rental_end_date:
        raise forms.ValidationError('End date must be after start date.')

    return cleaned_data
