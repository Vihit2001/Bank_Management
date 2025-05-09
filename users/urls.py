from django.urls import path
from .views import home,teller_dashboard,accountant_dashboard,manager_dashboard,add_staff,customer_service_representative_dashboard
from . import views

urlpatterns = [
    path('home/', home, name='home'),
    
    path('teller_dashboard/', teller_dashboard, name='teller_dashboard'),
    path('accountant_dashboard/', accountant_dashboard, name='accountant_dashboard'),
    path('manager_dashboard/', manager_dashboard, name='manager_dashboard'),
    path('customer_service_representative_dashboard/', customer_service_representative_dashboard, name='customer_service_representative_dashboard'),
    path('staff_list/',views.StaffListView.as_view() , name='staff_list'),
    path('staff_form/',add_staff , name='staff_form'),
]