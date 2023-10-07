# app_name/urls.py

from django.urls import path
from .views import CheckUsernameEmailView,SignUpUserView

urlpatterns = [
    path('check-user/', CheckUsernameEmailView.as_view(), name='check-user'),
    path('sign-up/',SignUpUserView.as_view(),name='sign-up')

]
