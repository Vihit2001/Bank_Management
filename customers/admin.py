from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class Customeradmin(admin.ModelAdmin):
    list_display=['first_name','last_name','age','gender','contact','address','email']

    
# @admin.register(AccountModel)
# class AccountModelAdmin(admin.ModelAdmin):
#     list_display = "__all__"