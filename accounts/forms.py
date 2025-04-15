from django import forms
from django.forms.widgets import Input
from .models import Customer, Accounts

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
        "full_name": Input(attrs={
            "type":"text",
            "placeholder":"Type in full_name",
        }),

        "email": Input(attrs={
            "type":"email",
            "placeholder":"Type in email",
        }),

        "phone_number": Input(attrs={
            "type":"number",
            "placeholder":"Type in phone_number",
        }),

        "address": Input(attrs={
            "type":"text",
            "placeholder":"Type in address",
        }),
        
        "dob": Input(attrs={
            "type":"date",
            "placeholder":"Type in dob",
        }),
        
        # "gender": Input(attrs={
        #     "type":"select",
        #     "placeholder":"Type in gender",
        # }),
        
        "pan_card": Input(attrs={
            "type":"number",
            "placeholder":"Type in pan_card",
        }),
        
        "aadhaar_number": Input(attrs={
            "type":"number",
            "placeholder":"Type in aadhaar_number",
        }),
        
        # "profile": Input(attrs={
        #     "type":"file",
        #     "placeholder":"Type in profile",
        # }),
    }

        
class AccountsForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = "__all__"
        exclude = ["account_holder"]
        widgets = {
        "account_no": Input(attrs={
            "type":"number",
            "placeholder":"Type in account_no",
        }),

        # "account_type": Input(attrs={
        #     "type":"select",
        #     "placeholder":"Type in account_type",
        # }),
        
        "branch_name": Input(attrs={
            "type":"text",
            "placeholder":"Type in branch_name",
        }),
        
        "ifsc_code": Input(attrs={
            "type":"text",
            "placeholder":"Type in ifsc_code",
        }),
        
        "balance": Input(attrs={
            "type":"number",
            "placeholder":"Type in balance",
        }),

        "date_opened": Input(attrs={
            "type":"date",
            "placeholder":"Type in date_opened ",
        }),
        }






























































# class CustomerAccountForm(forms.ModelForm):
#     full_name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     phone_number = forms.CharField(max_length=15)
#     address = forms.CharField(widget=forms.TextInput())
#     dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#     gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
#     pan_card = forms.CharField(max_length=10)
#     aadhaar_number = forms.CharField(max_length=12)
#     profile = forms.ImageField(required=False)

#     class Meta:
#         model = Accounts
#         fields = ['account_no', 'account_type', 'branch_name', 'ifsc_code', 'balance',
#                   'full_name', 'email', 'phone_number', 'address', 'dob', 'gender',
#                   'pan_card', 'aadhaar_number', 'profile']

#     def save(self, commit=True):
#         full_name = self.cleaned_data['full_name']
#         email = self.cleaned_data['email']
#         phone_number = self.cleaned_data['phone_number']
#         address = self.cleaned_data['address']
#         dob = self.cleaned_data['dob']
#         gender = self.cleaned_data['gender']
#         pan_card = self.cleaned_data['pan_card']
#         aadhaar_number = self.cleaned_data['aadhaar_number']
#         profile = self.cleaned_data.get('profile')  # optional field

#         customer = Customer.objects.create(
#             full_name=full_name,
#             email=email,
#             phone_number=phone_number,
#             address=address,
#             dob=dob,
#             gender=gender,
#             pan_card=pan_card,
#             aadhaar_number=aadhaar_number,
#             profile=profile
#         )

#         account = super().save(commit=False)
#         account.customer = customer
#         if commit:
#             account.save()
#         return account

