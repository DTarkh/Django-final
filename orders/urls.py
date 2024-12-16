from django.urls import path
from .views import CartView, AddCartItemView, UpdateCartItemView, DeleteCartItemView, OrderView, AddOrders

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<int:pk>/', AddCartItemView.as_view(), name='add_cart_item'),
    path('cart/update/<int:pk>/', UpdateCartItemView.as_view(), name='update_cart_item'),
    path('cart/delete/<int:pk>/', DeleteCartItemView.as_view(), name='delete_cart_item'),
    path('/', OrderView.as_view(), name='order'),
    path('/<int:pk>/', AddOrders.as_view(), name='add_orders'),
]