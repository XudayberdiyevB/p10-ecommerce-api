from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from paginations import CustomPageNumberPagination
from products.models import Product
from products.serializers import ProductListSerializer, ProductCreateSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ("category", "brand")
    ordering_fields = ("id", "price")
    search_fields = ("title", "category__title", "brand__title")
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductCreateSerializer
        return ProductListSerializer

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     query_params = self.request.query_params
    #     search_param = query_params.get("search")
    #     if search_param:
    #         queryset = queryset.filter(
    #             Q(title__icontains=search_param) | Q(category__title__icontains=search_param) | Q(
    #                 title__icontains=search_param)
    #         )
    #     price_from = query_params.get("price_from")
    #     price_to = query_params.get("price_to")
    #     if price_from:
    #         queryset = queryset.filter(price__gte=price_from)
    #     if price_to:
    #         queryset = queryset.filter(price__lte=price_to)
    #     categories = query_params.get("categories")  # ?categories=1,2,3
    #     if categories:
    #         queryset = queryset.filter(category_id__in=[int(cat_id) for cat_id in categories.split(",")])
    #     return queryset


class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    # serializer_class = ProductListSerializer
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return ProductCreateSerializer
        return ProductListSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)
    #
    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)
    #
    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)
