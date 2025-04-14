from django.contrib import admin
from .models import Customer,Accounts

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email","phone_number","address","dob","gender","pan_card","aadhaar_number","profile"]

@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ["account_no", "account_type","account_holder","branch_name","ifsc_code","balance","date_opened"]
