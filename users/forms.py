from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Staff
# from django.contrib.auth.forms import ReadOnlyPasswordHashField

class CustomUserForm(UserCreationForm):
    class Meta:
        model=CustomUser
        # fields=['username','password1','password2','role']
        exclude=['groups','user_permissions','last_login','password','is_superuser', 'is_staff', 'is_active','date_joined']

class StaffCreationForm(forms.ModelForm):
    class Meta:
        model = Staff
        exclude=['user']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(attrs={'type': 'text'}),
            'address': forms.TextInput(attrs={'type': 'text'}),
            'qualification': forms.TextInput(attrs={'type': 'text'}),
            'salary': forms.NumberInput(attrs={'type': 'text'}),
        }
        
        