from django.db import models


class Order(models.Model):
    customer = models.CharField(null=True, max_length=30)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer}"


class Cart(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, related_name="user_order")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="product")
    total_price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orders")
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"


class Payment(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="payment_cart")
    price = models.IntegerField()
    provider = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cart}"