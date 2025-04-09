from django.shortcuts import render
from customers.forms import CustomerForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterView(CreateView):
    form_class = CustomerForm
    success_url = reverse_lazy("home")
    template_name = "customers/signup.html"