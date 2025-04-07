from django.urls import path
from .views import home,teller_dashboard,customer_dashboard

urlpatterns = [
    path('home/', home, name='home'),
    path('teller_dashboard/', teller_dashboard, name='teller_dashboard'),
    path('customer_dashboard/', customer_dashboard, name='customer_dashboard'),
]