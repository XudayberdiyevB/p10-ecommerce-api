from django.urls import path

from products.views import get_products_list, get_product, category, category_detail

urlpatterns = [
    # @api_view
    path("categories/", category, name="category-list-create"),
    path("categories/<int:pk>/", category_detail, name="category-detail"),
    path("", get_products_list, name="products-list"),
    # path("<int:pk>/", get_product, name="products-detail")
    path("<slug:slug>/", get_product, name="products-detail"),
]
