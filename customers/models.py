from django.db import models

# Create your models here.
class Customer(models.Model):
    Gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
        ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=Gender_choices,default='O')
    address = models.TextField()
    contact = models.IntegerField(max_length=10,unique=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.first_name} ({self.email})"
    
class Account(models.Model):
    Account_type_choices= [
        ('SAVING','Saving'),
        ('CURRENT','Current')
        ]
    Status_choices = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('SUSPENDED', 'Suspended')
        ]
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="accounts")
    account_number = models.CharField(max_length=15,unique=True)
    account_type = models.CharField(max_length=10,choices=Account_type_choices,default='SAVING')
    status = models.CharField(max_length=10, choices=Status_choices, default='ACTIVE')
    account_balance = models.IntegerField()
    account_branch = models.CharField(max_length=20) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_type} - {self.account_number} ({self.customer.first_name})"