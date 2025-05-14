from django.shortcuts import render, redirect, reverse
import stripe
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import *
from .utils import *
from .cart import Cart

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def shop_view(request):
    products_list = stripe.Product.list()
    products = []

    for product in products_list['data']:
        if product.get('metadata', {}).get('category') == "shop":
            products.append(get_product_details(product))

    return render(request, 'shop.html', {'products': products})

def merch_view(request, product_id):
    product = stripe.Product.retrieve(product_id)
    product_details = get_product_details(product)

    cart = Cart(request)
    product_details['in_cart'] = product_id in cart.cart_session

    return render(request, 'merch.html', {'product': product_details})

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return redirect('merch', product_id)



def payment_successful(request):
    checkout_session_id = request.GET.get('session_id', None)

    if checkout_session_id:
        session = stripe.checkout.Session.retrieve(checkout_session_id)
        customer_id = session.customer
        customer = stripe.Customer.retrieve(customer_id)

        line_item = stripe.checkout.Session.list_line_items(checkout_session_id).data[0]
        UserPayment.objects.get_or_create(
            stripe_customer = customer_id,
            stripe_checkout_id = checkout_session_id,
            stripe_product_id = line_item.price.product,
            product_name = line_item.description,
            quantity = line_item.quantity,
            price = line_item.price.unit_amount / 100.0,
            currency = line_item.price.currency,
            has_paid = True,
        )

    return render(request, 'payment_successful.html', {'customer': customer})

def payment_cancelled(request):
    return render(request, 'payment_cancelled.html')

@require_POST
@csrf_exempt
def stripe_webhook(request):
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    payload = request.body
    signature_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, signature_header, endpoint_secret
        )
    except:
        return HttpResponse(status=400)

    if event['type'] == 'check.session.completed':
        session = event['data']['object']
        checkout_session_id = session.get('id')
        user_payment = UserPayment.objects.get(stripe_checkout_id=checkout_session_id)
        user_payment.has_paid = True
        user_payment.save()

    return HttpResponse(status=200)