from django.views.generic import *
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Car, Booking
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Car

def car_list(request):
    car_objects = Car.objects.all().order_by('?')
    if request.method == 'GET':
        search =request.GET.get('S')
        if search != None :
             car_objects = Car.objects.filter(car_name__icontains=search).order_by('?')
        else:
            car_objects = Car.objects.all().order_by('?')

    paginator = Paginator(car_objects, 9)  # Number of items per page

    page = request.GET.get('page')
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        cars = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        cars = paginator.page(paginator.num_pages)

    return render(request, 'home/carlist.html', {'cars': cars})



class car_details(DetailView):
  model = Car
  template_name = 'home/car_details.html'
  context_object_name = 'product'
  pk_url_kwarg = 'id'

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render, redirect
from django.utils.timezone import datetime
from .models import Car, Booking

@login_required
def book_car(request, id):
    car = Car.objects.get(id=id)
    if request.method == 'POST':
        # Retrieve form data
        rental_start_date = datetime.strptime(request.POST.get('rental_start_date'), '%Y-%m-%d')
        rental_end_date = datetime.strptime(request.POST.get('rental_end_date'), '%Y-%m-%d')
        pickup_location = request.POST.get('pickup_location')
        dropoff_location = request.POST.get('dropoff_location')
        phone = request.POST.get('phone')
        # Retrieve car object



        # Create a new Booking object and save it to the database
        booking = Booking.objects.create(car=car, customer=request.user, rental_start_date=rental_start_date, rental_end_date=rental_end_date, phone=phone, pickup_location=pickup_location, dropoff_location=dropoff_location)

        subject = 'New car booked'
        html_content = render_to_string('home/email.html', {'booking': booking, })
        send_mail(
                    subject,
                    'from {{request.user.email}}',
                    'KhulnaCarRental.com',
                    ['mpias3721@gmail.com'],
                    fail_silently=False,
                    html_message=html_content,
                )
        return redirect('booking_details')

    else:
        return render(request, 'home/book_car.html', {'car': car})



@login_required
def booking_details(request):
    bookings = Booking.objects.filter(customer=request.user).order_by('-id')

    for booking in bookings:

        booking.num_days = (booking.rental_end_date - booking.rental_start_date).days
        total_price = booking.num_days * booking.car.cost_par_day
        booking.total_price = total_price

    return render(request, 'home/booking_details.html', {'bookings': bookings})


from easy_pdf.views import PDFTemplateView
from django.shortcuts import get_object_or_404
from .models import Booking
from datetime import timedelta

class BookingPDFView(PDFTemplateView):
    template_name = 'home/pdf.html'

    def get_context_data(self, **kwargs):
        context = super(BookingPDFView, self).get_context_data(**kwargs)
        booking_id = self.kwargs['booking_id']
        booking = get_object_or_404(Booking, pk=booking_id)

        # Calculate the number of days and total price
        booking.num_days = (booking.rental_end_date - booking.rental_start_date).days
        if booking.num_days < 1:
            booking.num_days = 1  # Ensure minimum charge for at least one day
        booking.total_price = booking.num_days * booking.car.cost_par_day

        context['booking'] = booking
        return context

    def render_to_response(self, context, **response_kwargs):
        response = super(BookingPDFView, self).render_to_response(context, **response_kwargs)
        response['Content-Disposition'] = 'attachment; filename="Booking_{}.pdf"'.format(context['booking'].id)
        return response





def success_page(request):
    return render(request, 'home/success.html')
def contact(request):
    return render(request, 'home/contact.html')