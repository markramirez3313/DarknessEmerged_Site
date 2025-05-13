from django.shortcuts import render, redirect, reverse
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def merch_view(request):
    product_id = 'prod_SIawWYkhxmlUwJ'
    product = stripe.Product.retrieve(product_id)
    prices = stripe.Price.list(product=product_id)
    price = prices.data[0]
    product_price = price.unit_amount / 100.0

    if request.method == 'POST':
        price_id = request.POST.get('price_id')
        quantity = int(request.POST.get('quantity'))
        checkout_session = stripe.checkout.Session.create(
            line_items = [
                {
                    'price': price_id,
                    'quantity': quantity,
                },
            ],
            payment_method_types = ['card'],
            mode = 'payment',
            customer_creation = 'always',
            success_url = f'{settings.BASE_URL}{reverse("payment_successful")}?session_id={{CHECKOUT_SESSION_ID}}',
            cancel_url = f'{settings.BASE_URL}{reverse("payment_cancelled")}',
        )
        return redirect(checkout_session.url, code=303)
    return render(request, 'merch.html', {'product': product, 'product_price': product_price})

def payment_successful(request):
    return render(request, 'payment_successful.html')

def payment_cancelled(request):
    return render(request, 'payment_cancelled.html')