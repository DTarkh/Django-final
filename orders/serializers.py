from rest_framework import serializers
from .models import Cart, CartItem
from store.models import Product

class CartItemSerializer(serializers.ModelSerializer):
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