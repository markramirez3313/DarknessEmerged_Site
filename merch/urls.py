from django.urls import path
from .views import *

urlpatterns = [
    path('', shop_view, name="shop"),
    path('merch/<product_id>', merch_view, name="merch"),
    path('cart/', cart_view, name='cart'),
    path('payment_successful/', payment_successful, name='payment_successful'),
    path('payment_cancelled/', payment_cancelled, name='payment_cancelled'),
    path('stripe_webhook/', stripe_webhook, name='stripe_webhook'),
    path('add_to_cart/<product_id>', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<product_id>', remove_from_cart, name='remove_from_cart'),
    path('hx_menu_cart/', hx_menu_cart, name='hx_menu_cart'),
    path('update_checkout/<product_id>', update_checkout, name='update_checkout'),
    path('checkout/', checkout_view, name='checkout'),
]