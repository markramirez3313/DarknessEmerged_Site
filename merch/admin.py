from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ShippingInfo)
admin.site.register(CheckoutSession)
admin.site.register(ProductSize)
admin.site.register(ProductVariation)