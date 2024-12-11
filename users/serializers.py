
from rest_framework_simplejwt.serializers import TokenObtainSerializer


class CustomTokenObtainSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        permissions = user.get_all_permissions()
        token['permissions'] = list(permissions)

        return token