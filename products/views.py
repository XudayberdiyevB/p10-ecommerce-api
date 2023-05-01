from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from products.models import Product, Category
from products.serializers import ProductListSerializer, CategorySerializer


@api_view(["GET"])
def get_products_list(request):
    products = Product.objects.order_by("-id")
    # products_data = [{"id": product.id, "title": product.title} for product in products]
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_product(request, slug):
    # try:
    #     product = Product.objects.get(slug=slug)
    # except Product.DoesNotExist:
    #     raise Http404
    product = get_object_or_404(Product, slug=slug)
    serializer = ProductListSerializer(product)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def category(request):
    serializer_class = CategorySerializer
    queryset = Category.objects.order_by("position")
    serializer = serializer_class(queryset, many=True)
    if request.method == "POST":
        serializer = serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def category_detail(request, pk):
    serializer_class = CategorySerializer
    cat = get_object_or_404(Category, pk=pk)
    if request.method == "PUT":
        serializer = serializer_class(instance=cat, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    if request.method == "DELETE":
        cat.delete()
        return Response(f"Category ID {cat.id} deleted.", status=status.HTTP_204_NO_CONTENT)
    serializer = serializer_class(cat)
    return Response(serializer.data)
