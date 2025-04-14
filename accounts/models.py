from django.db import models

# Create your models here.
class Customer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    pan_card = models.CharField(max_length=10)
    aadhaar_number = models.CharField(max_length=12, blank=True, null=True)
    profile = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.full_name
    
class Accounts(models.Model):
    ACCOUNT_TYPES= [
        ('SAVINGS', 'Savings'),
        ('CURRENT', 'Current'),
        ('FIXED', 'Fixed Deposit'),
    ]
    
    account_no = models.IntegerField(unique=True)
    account_type = models.CharField(max_length=12,choices=ACCOUNT_TYPES)
    account_holder = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='accounts')
    branch_name = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=10)
    balance = models.DecimalField(max_digits=19,decimal_places=2)
    date_opened = models.DateField(auto_now_add=True)
    
    
    