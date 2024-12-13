from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Cart, CartItem
from store.models import Product
from .serializers import CartSerializer, CartItemSerializer

class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        cart, _ = Cart.objects.get_or_create(user=request.user)

        if Product.stock > 0:
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

            if not created:
                cart_item.quantity += 1
            else:
                cart_item.quantity = 1
            cart_item.save()

        return Response({"message": "Item added to cart"}, status=status.HTTP_200_OK)

class UpdateCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            cart_item = CartItem.objects.get(pk=pk, cart__user=request.user)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)

        new_quantity = request.data.get('quantity', 0)

        if new_quantity == 0:
            cart_item.delete()
            return Response({"message": "Cart item deleted"}, status=status.HTTP_200_OK)

        if new_quantity > cart_item.book.stock:
            return Response({"error": "Insufficient stock"}, status=status.HTTP_400_BAD_REQUEST)

        cart_item.quantity = new_quantity
        cart_item.save()
        return Response({"message": "Cart item updated"}, status=status.HTTP_200_OK)

class DeleteCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            cart_item = CartItem.objects.get(pk=pk, cart__user=request.user)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)

        cart_item.delete()
        return Response({"message": "Cart item deleted"}, status=status.HTTP_200_OK)