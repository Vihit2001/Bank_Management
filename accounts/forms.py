from django import forms
from .models import Customer, Accounts

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        
class AccountsForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = "__all__"































































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

