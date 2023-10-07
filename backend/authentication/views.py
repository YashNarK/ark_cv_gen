from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class CheckUsernameEmailView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='username_or_email',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description='Username or email address to search for (either one is accepted).'
            ),
        ],
        responses={
            200: openapi.Response(
                name='username_or_email',  # Define the name of the response
                description='Response with the username or email',  # Define response description
                schema=openapi.Schema(type=openapi.TYPE_STRING),  # Define response schema
            ),
            404: openapi.Response(
                description='User not found',  # Define response description
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error_message': openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
        }
    )
    def get(self, request):
        username_or_email = request.query_params.get('username_or_email', None)
        
        if username_or_email:
            # Try to find a user by username
            user = CustomUser.objects.filter(username=username_or_email).first()
            
            if not user:
                # If not found by username, try to find by email
                user = CustomUser.objects.filter(email=username_or_email).first()
            
            if user:
                serializer = CheckUsernameEmailSerializer(user)
                return Response(serializer.data)
            else:
                return Response({'message': 'User not found'}, status=404)
        else:
            return Response({'message': 'Missing username_or_email parameter'}, status=400)


class SignUpUserView(APIView):
    @swagger_auto_schema(request_body=BasicSignUpSerializer)
    def post(self, request):
        # Deserialize and validate the request data using the BasicSignUpSerializer
        serializer = BasicSignUpSerializer(data=request.data)
        
        if serializer.is_valid():
            # Create a new user instance with validated data
            user = serializer.save()
            # Return a success response with the user data
            return Response({'message': 'User successfully created', 'user_id': user.id}, status=status.HTTP_201_CREATED)
        
        # If validation fails, return an error response with validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

