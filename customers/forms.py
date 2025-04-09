from django import forms
from .models import Customer
from django.forms.widgets import Input

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
        "first_name": Input(attrs={
            "type":"text",
            "placeholder":"Type in first_name",
        }),
        "last_name": Input(attrs={
            "type":"text",
            "placeholder":"Type in last_name",
        }),
        "age": Input(attrs={
            "type":"number",
            "placeholder":"Type age",
        }),
        "gender": Input(attrs={
            "type":"select",
            "placeholder":"Type in gender",
        }),
        "address": Input(attrs={
            "type":"text",
            "placeholder":"Type in address",
        }),
        "contact": Input(attrs={
            "type":"number",
            "placeholder":"Type in contact",
        }),
        "email": Input(attrs={
            "type":"email",
            "placeholder":"Type in email",
        }),
        }
    