from rest_framework import serializers
from .models import CustomUser

# Check whether username/email already exists or not serializer 
class CheckUsernameEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','email']# Sign up as a user serializer

# Sign-up
class BasicSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','email','first_name','last_name','password','date_of_birth']
    
    # hash and salt the password
    def create(self, validated_data):
        from django.contrib.auth.hashers import make_password
        password=make_password(validated_data['password'])

        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            date_of_birth=validated_data['date_of_birth'],
            password=password  # Assign the hashed password
        )
        return user