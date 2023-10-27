from django.contrib import admin
from django.urls import include, path
from checkoutbook.views import display_order,pay_order

app_name = 'checkoutbook'

urlpatterns = [
    path('display-order/', display_order, name='display_order'),
    path('pay-order/', pay_order, name='pay_order'),
]