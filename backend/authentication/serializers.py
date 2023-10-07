from rest_framework import serializers
from .models import CustomUser

# Check whether username/email already exists or not serializer
class CheckUsernameEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','email']
# Sign up as a user serializer