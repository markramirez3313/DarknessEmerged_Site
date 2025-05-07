import os
import stripe
from flask import Flask, redirect, request

app = Flask(__name__,
                static_url_path='',
                static_folder='public')

stripe.api_key = 'pk_live_51RKMZ6DV4IH0qgqQmXm1GOjj9B72IYROiN06hEbTZ12ttTqINkTql4ywvqQIHiwYxl5PCodlIh4cHMMIx9CQRuIF00NZY8qRmj'

YOUR_DOMAIN = 'https://www.darknessemerged.com'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items = [
                {
                    'price': '{{PRICE_ID}}',
                    'quantinty':1,
                },
            ],
            mode = 'payment',
            ui_mode = 'embedded',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
            automatic_tax={'enabled': True},
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

if __name__ == '__main__':
  app.run(port=4242)