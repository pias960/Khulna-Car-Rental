from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm, PasswordResetForm
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class OTPConfirmationForm(forms.Form):
    otp_code = forms.CharField(label='OTP Code', max_length=6)

class passwordChangeForm(PasswordChangeForm):
    PasswordChangeForm.base_fields['old_password'].widget.attrs['class'] = 'form-control'
    PasswordChangeForm.base_fields['new_password1'].widget.attrs['class'] = 'form-control'
    PasswordChangeForm.base_fields['new_password2'].widget.attrs['class'] = 'form-control'
    
class setpasswordform(SetPasswordForm):
    PasswordChangeForm.base_fields['new_password1'].widget.attrs['class'] = 'form-control'
    PasswordChangeForm.base_fields['new_password2'].widget.attrs['class'] = 'form-control'
    
class passwordresetform(PasswordResetForm):
    PasswordResetForm.base_fields['email'].widget.attrs['class'] = 'form-control'

