from django.urls import path
from .views import *

urlpatterns = [
    path('', merch_view, name="merch"),
    path('payment_successful/', payment_successful, name='payment_successful'),
    path('payment_cancelled/', payment_cancelled, name='payment_cancelled'),
]