from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View, generic

from .forms import CustomUserForm, StaffCreationForm
from .models import CustomUser, Staff


def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirect based on user role
            if user.is_admin:
                return redirect("manager_dashboard")  # Manager Dashboard
            elif user.is_teller:
                return redirect("teller_dashboard")  # Teller Dashboard
            elif user.is_accountant:
                return redirect("accountant_dashboard")  # accountant Dashboard
            elif user.is_customer_service_representative:
                return redirect(
                    "customer_service_representative_dashboard"
                )  # CSR Dashboard
            else:
                messages.error(request, "Invalid role assigned.")
                return redirect("home")
        else:
            return render(
                request, "users/home.html", {"error_message": "Invalid credentials"}
            )

    return render(request, "users/home.html")


# Mnager Dashboard View
@login_required
def manager_dashboard(request):
    return render(request, "users/manager_dashboard.html")


# Teller Dashboard View
@login_required
def teller_dashboard(request):
    return render(request, "users/teller_dashboard.html")


@login_required
def accountant_dashboard(request):
    return render(request, "users/accountant_dashboard.html")


@login_required
def customer_service_representative_dashboard(request):
    return render(request, "users/customer_service_representative_dashboard.html")


def add_staff(request):
    if request.method == "POST":
        userobj = CustomUserForm(request.POST)
        staff = StaffCreationForm(request.POST)
        if userobj.is_valid() and staff.is_valid():
            user = userobj.save()
            # st = staff.save(commit=False)
            # st.user = user
            # st.save() 
            st = Staff.objects.create(user=user, **staff.cleaned_data)
            return redirect("staff_list")
        print("Custom Form Errors:", userobj.errors)
        print("Staff Form Errors:", staff.errors)
        return render(
            request,
            "users/staff_form.html",
            context={"userobj": userobj, "staff": staff},
        )

    else:
        userobj = CustomUserForm()
        staff = StaffCreationForm()
        return render(
            request,
            "users/staff_form.html",
            context={"userobj": userobj, "staff": staff},
        )


class StaffListView(generic.ListView):
    model = Staff
    context_object_name = "staff"
    template_name = "users/staff_list.html"
