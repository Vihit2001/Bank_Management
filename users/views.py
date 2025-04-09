from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Redirect based on user role
            if user.is_admin:
                return redirect('manager_dashboard')  # Manager Dashboard
            elif user.is_teller:
                return redirect('teller_dashboard')  # Teller Dashboard
            elif user.is_customer:
                return redirect('customer_dashboard')  # Customer Dashboard
            else:
                messages.error(request, "Invalid role assigned.")
                return redirect('home')
        else:
            return render(request, 'users/home.html', {'error_message': 'Invalid credentials'})
    
    return render(request, 'users/home.html')

# Mnager Dashboard View
@login_required
def manager_dashboard(request):
    return render(request, 'users/manager_dashboard.html')

# Teller Dashboard View
@login_required
def teller_dashboard(request):
    return render(request, 'users/teller_dashboard.html')

# Customer Dashboard View
@login_required
def customer_dashboard(request):
    return render(request, 'users/customer_dashboard.html')
