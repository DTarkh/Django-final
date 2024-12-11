from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer



@api_view(['GET'])
def product_list(request):
    product_title = request.GET.get('product_title')
    category = request.GET.getlist('category')  # Use getlist to handle multiple categories
    min_price = request.GET.get('minPrice')
    max_price = request.GET.get('maxPrice')
    price_order = request.GET.get('price_order')  # "asc" or "desc"
    rating_order = request.GET.get('rating_order')  # "desc"


    query_set = Product.objects.all()

    if product_title:
        query_set = query_set.filter(title__icontains=product_title)

    if category:
        query_set = query_set.filter(category__id__in=category)

    if min_price and max_price:
        query_set = query_set.filter(price__gte=min_price, price__lte=max_price)
    elif min_price:
        query_set = query_set.filter(price__gte=min_price)
    elif max_price:
        query_set = query_set.filter(price__lte=max_price)

        # Order by price
    if price_order == "asc":
        query_set = query_set.order_by('price')  # Ascending order
    elif price_order == "desc":
        query_set = query_set.order_by('-price')  # Descending order

        # Order by rating (descending)
    if rating_order == "desc":
        # Assuming a related `rating` model or field; use Avg if ratings are in another model
        query_set = query_set.order_by('-rating')

    # Serialize the filtered query set
    serialized_products = ProductSerializer(query_set, many=True)

    return Response(serialized_products.data)
@api_view()
def product_detail(request,id):
    product = get_object_or_404(Product, pk=id)
    serialized_products = ProductSerializer(product)
    return Response(serialized_products.data)