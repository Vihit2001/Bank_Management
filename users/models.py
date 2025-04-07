from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("teller", "Teller"),
        ("customer", "Customer"),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    @property
    def is_admin(self):
        return self.role and self.role == "admin"

    @property
    def is_teller(self):

        return self.role and self.role == "teller"

    @property
    def is_customer(self):
        return self.role and self.role == "customer"

    def __str__(self):
        return f"{self.username} ({self.role})"
