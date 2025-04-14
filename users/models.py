from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("teller", "Teller"),
        ("accountant", "Accountant"),
        ("customer_service_representative","customer_service_representative")
    ]
    
    role = models.CharField(choices=ROLE_CHOICES)

    @property
    def is_admin(self):
        return self.role and self.role == "admin"

    @property
    def is_teller(self):
        return self.role and self.role == "teller"

    @property
    def is_accountant(self):
        return self.role and self.role == "accountant"

    @property
    def is_customer_service_representative(self):
        return self.role and self.role == "customer_service_representative"

    def __str__(self):
        return f"{self.username} ({self.role})"
