from django.urls import path
from . import views

urlpatterns = [
    path('accounts_form/',views.AccountCreateView.as_view(),name='accounts_form'),
    path('accounts_list/',views.AccountListView.as_view(),name='accounts_list'),
]