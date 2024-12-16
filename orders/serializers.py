from rest_framework import serializers
from .models import Cart, CartItem, OrderItem, Order
from store.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'thumbnail']  # Include only the necessary fields

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Use the ProductSerializer here
    total = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity', 'total']
        read_only_fields = ['cart', 'total']

    def get_total(self, obj):
        return obj.quantity * obj.product.price

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, source='cartitem_set', read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']
        read_only_fields = ['user', 'items']



class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    total = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'total']
        read_only_fields = ['order', 'product', 'quantity', 'total']

    def get_total(self, obj):
        return obj.quantity * obj.product.price

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, source='orderitem_set', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'items']
        read_only_fields = ['user', 'items']