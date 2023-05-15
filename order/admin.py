from django.contrib import admin

from order.models import Order, Payment, Cart


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "created_at"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "total_price"]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["cart", "price"]
