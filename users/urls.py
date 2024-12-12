# from django.urls import path
# from . import views
# from rest_framework_simplejwt.views import TokenRefreshView
#
#
#
# urlpatterns = [
#     path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
# ]

from django.urls import path
from .views import register_user, login_user

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
]