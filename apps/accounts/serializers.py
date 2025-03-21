from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class RegisterSerializer(TokenObtainPairSerializer):
    username = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255, read_only=True)

    def validate(self, attrs):
        data = super().validate(attrs)

        data['username'] = self.user.username
        data['email'] = self.user.email

        return data