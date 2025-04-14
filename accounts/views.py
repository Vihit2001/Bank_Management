from django.shortcuts import render,redirect
from django.views import generic
from .models import Accounts
from django.contrib import messages
from .forms import CustomerForm , AccountsForm

# Create your views here.
class AccountCreateView(generic.View):
    def create_Account(request):
        if request.method == "POST":
            customer_form = CustomerForm(
                request.POST, instance=request.user, prefix="name")
            account_form = AccountsForm(
                request.POST, instance=request.accounts.customer, prefix="account")
            if all([customer_form.is_valid() and account_form.is_valid()]):
                customer_form.save()
                account_form.save()
                

                # prof.university = uni
                # prof.work = wor
                # prof.save()

                messages.success(request, _(
                    "Customer account was successfully created!"))
                return redirect("account_list")
            else:
                messages.error(request, _("Please correct the error below."))
        else:
            customer_form= customer_form(instance=request.user, prefix="user")
            account_form = account_form(instance=request.accounts.customer)
           
            return render(
                request,
                "accounts/accounts_form.html",
                {"customer_form": customer_form, "account_form": account_form},
            )
    # model = Accounts
    # fields = "__all__"
    # form_class =CustomerAccountForm
    # template_name='accounts/accounts_form.html'
    # success_url = "/accounts/accounts_list/"
    
class AccountListView(generic.ListView):
    model= Accounts
    context_object_name= "accounts"
    template_name = 'accounts/accounts_list.html'

