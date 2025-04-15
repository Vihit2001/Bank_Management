from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Accounts, Customer
from django.contrib import messages
from .forms import CustomerForm, AccountsForm


# Create your views here.
class AccountCreateView(View):
    def get(self, request):
        customer_form = CustomerForm()
        account_form = AccountsForm()
        return render(
            request,
            "accounts/accounts_form.html",
            context={"customer_form": customer_form, "account_form": account_form},
        )

    def post(self, request):
        customer_form = CustomerForm(request.POST,request.FILES)
        account_form = AccountsForm(request.POST,request.FILES)
        if customer_form.is_valid() and account_form.is_valid():
            cr =customer_form.save()
            ac = account_form.save(commit=False)
            ac.account_holder = cr
            ac.save()

            return redirect("accounts_list")
        print("Customer Form Errors:", customer_form.errors)
        print("Account Form Errors:", account_form.errors)
        
        return render(
            request,
            "accounts/accounts_form.html",
            context={"customer_form": customer_form, "account_form": account_form},
        )

    # def get(self,request):
    #     if request.method == "GET":
    #         customer_form = customer_form()
    #         account_form = account_form()

    #         return render(
    #             request,
    #             "accounts/accounts_form.html",
    #             {
    #                 "customer_form": customer_form,
    #                 "account_form": account_form,
    #             },
    #         )

    # def post(self,request):
    #     if request.method == "POST":
    #         customer_form = customer_form()
    #         cust_form = CustomerForm(request.POST,instance=customer_form)
    #         account_form = account_form()
    #         ac_form = AccountsForm(request.POST,instance=account_form)
    #         if customer_form.is_valid() and account_form.is_valid():
    #             customer = cust_form.save()
    #             account = ac_form.save()

    #             # prof.university = uni
    #             # prof.work = wor
    #             # prof.save()
    #             return redirect("accounts_list")
    #         else:
    #             messages.error(request,("Please correct the error below."))

    # model = Accounts
    # fields = "__all__"
    # form_class =CustomerAccountForm
    # template_name='accounts/accounts_form.html'
    # success_url = "/accounts/accounts_list/"


class AccountListView(generic.ListView):
    model = Accounts
    context_object_name = "accounts"
    template_name = "accounts/accounts_list.html"
