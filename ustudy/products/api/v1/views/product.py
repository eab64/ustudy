from datetime import datetime
from rest_framework.generics import GenericAPIView

from rest_framework.response import Response

from products.models.product import Product

from products.api.v1.serializers.product_serializers import ProductSerializer
from products.api.v1.serializers.category_serializers import CategorySerializer


class ProductListAPIView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductRetrieveAPIView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(pk=self.kwargs['product_id'])
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class ProductCategoryListAPIView(GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        product = Product.objects.get(pk=self.kwargs['product_id'])
        categories = product.categories.all()
        ser_data = serializer(categories, many=True).data
        return Response(ser_data)