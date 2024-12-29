
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view 
from django.contrib.auth.views import *
from .forms import *
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import views as auth_view 
from django.contrib.auth.views import *

urlpatterns = [

    path('login/', views.login_with_otp, name='login'),
    path('verify/', views.otp_confirmation, name='verify_otp'),
    path('register/', views.register, name='register'),
    #path('out/', auth_view.LogoutView.as_view(next_page='login'), name='logout' ),
    path('logout/', views.custom_logout, name='logout'),
     path('', views.home, name='home'),
    # path('carlist/', views.car_list, name="car_list"),
    # path('createOrder/', views.order_created, name="order_create"),

     ########password change done url###########
    path("passwordchangedone/", auth_view.PasswordChangeDoneView.as_view(template_name='login/passwordchangedone.html'), 
         name="passswordchangedone"),

    ########password change url###########
    path('password_change/',login_required( auth_view.PasswordChangeView.as_view(template_name='login/passwordchange.html',
              form_class=PasswordChangeForm, success_url='passswordchangedone')), name='passwordchange'),
    

    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='login/passwordreset.html',
              form_class=passwordresetform, ), name='password-reset'),
            
    path("password_reset/done/", auth_view.PasswordResetDoneView.as_view(template_name='login/passwordresetdone.html'), 
    name="password_reset_done"),


     path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='login/passwordresetconfirm.html',
              form_class=setpasswordform, ), name='password_reset_confirm'),

     path("password_reset_complete/",               auth_view.PasswordResetCompleteView.as_view(template_name='login/passwordresetcomplete.html'), 
    name="password_reset_complete"),
   



    

]