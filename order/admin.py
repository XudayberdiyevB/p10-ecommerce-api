from django.contrib import admin

from order.models import order, cart, payment


# Register your models here.
@admin.register(order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "created_at"]


@admin.register(cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "total_price"]


@admin.register(payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["cart", "price"]
