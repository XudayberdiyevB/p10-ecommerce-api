from django.urls import path

from products.views import (
    ProductListCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductRetrieveView
)

urlpatterns = [
    path("", ProductListCreateView.as_view(), name="products_list_create"),
    # path("<int:pk>/", ProductRetrieveView.as_view(), name="product_read"),
    # path("<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    # path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="product_detail")
]
