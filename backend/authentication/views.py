from rest_framework import generics, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CheckUsernameEmailSerializer

class CheckUsernameEmailView(generics.RetrieveAPIView):
    serializer_class = CheckUsernameEmailSerializer
    def get_object(self):
        # Get the username or email from the URL query parameters
        username_or_email = self.request.query_params.get('username_or_email')

        # Query the CustomUser model to check if the username or email exists
        try:
            user = CustomUser.objects.get(username=username_or_email)
            return user
        except CustomUser.DoesNotExist:
            try:
                user = CustomUser.objects.get(email=username_or_email)
                return user
            except CustomUser.DoesNotExist:
                return None