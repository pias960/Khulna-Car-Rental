from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
# from django_otp.forms import OTPAuthenticationForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


from datetime import timedelta

from datetime import timedelta
from django.template.loader import render_to_string
from .forms import *
import random


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            if password != confirm_password:
                messages.error(request, "Passwords do not match")
                return redirect('register')  # Redirect back to registration page
            try:
                validate_password(password)  # Check if password meets Django's built-in validators
            except ValidationError as e:
                messages.error(request, e)  # If not, display error message
                return redirect('register')

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken")
                return redirect('register')  # Redirect back to registration page

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered")
                return redirect('register')  # Redirect back to registration page

            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            messages.success(request, f'Account created for {username}!')
            return redirect('success_page')  # Redirect to login page

        return render(request, 'login/register.html')


def login_with_otp(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_authenticated:  # Check if the user is authenticated
                otp_code = ''.join(random.choices('0123456789', k=6))  # Generate a 6-digit OTP code

                # Send OTP code via email
                subject = 'Your OTP Code'
                html_content = render_to_string('login/otp_email_templates.html', {'otp_code': otp_code})
                expiration_time = timezone.now() + timedelta(minutes=2)
                request.session['otp_expiration_time'] = expiration_time.strftime('%Y-%m-%d %H:%M:%S')

                send_mail(
                    subject,
                    'Verify your otp',
                    'KhulnaCarRental.com',
                    [user.email],
                    fail_silently=False,
                    html_message=html_content,
                )

                # Store OTP code in session
                request.session['otp_code'] = otp_code
                request.session['user_id'] = user.id  # Store user id in session
                return redirect('verify_otp')
            else:
                messages.error(request, "Username or password is Wrong")
                return redirect('login')

    return render(request, 'login/otp_login.html',)

def otp_confirmation(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        user_id = request.session.get('user_id')
        if user_id is None:
            return redirect('login')  # Redirect to login page if user_id is not found in session

        user = User.objects.get(pk=user_id)
        if request.method == 'POST':
            form = OTPConfirmationForm(request.POST)
            if form.is_valid():
                entered_otp_code = form.cleaned_data['otp_code']
                stored_otp_code = request.session.get('otp_code')
                if entered_otp_code == stored_otp_code:
                    # OTP code matches, authenticate user
                    login(request, user)
                    # Optionally, clear OTP code and user_id from session
                    del request.session['otp_code']
                    del request.session['user_id']
                    return redirect('home')  # Redirect to home page after successful authentication
                else:
                    messages.error(request, "OTP code does not match")
                 # Redirect back to registration page

        else:
            form = OTPConfirmationForm()
    return render(request, 'login/verify_otp.html', {'form': form})

from car.models import Car

def home(request):
    cars = Car.objects.all().order_by('?')[1:10]
    return render(request, 'home/home.html', {'cars': cars})
from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('login')

