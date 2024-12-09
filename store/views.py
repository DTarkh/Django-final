from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


@api_view()
def product_list(request):
    query_set = Product.objects.all()
    serialized_products = ProductSerializer(query_set, many=True)

    return Response(serialized_products.data)
@api_view()
def product_detail(request,id):
    product = get_object_or_404(Product, pk=id)
    serialized_products = ProductSerializer(product)
    return Response(serialized_products.data)