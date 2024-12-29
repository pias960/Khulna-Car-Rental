from django.contrib import admin
from django.urls import path
from .views import *
from . import views


urlpatterns = [

    path("car_list/", views.car_list, name="car-list"),
    path("car_details/<int:id>/", views.car_details.as_view(), name="car-details"),
    path('book-car/<int:id>/', views.book_car, name='book-car'),
    path('success/', views.success_page, name='success_page'),
    path('contact/', views.contact, name='contact'),
    path('booking_pdf/<int:booking_id>/', BookingPDFView.as_view(), name='booking_pdf'),
    path('booking_details/', views.booking_details, name='booking_details'),



]