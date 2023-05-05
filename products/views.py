from rest_framework import generics

from products.models import Product
from products.serializers import ProductListSerializer, ProductCreateSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()

    # serializer_class = ProductListSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductCreateSerializer
        return ProductListSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)


# class ProductListView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class ProductCreateView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


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
