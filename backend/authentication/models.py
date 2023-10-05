from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
# username: A unique username for the user. This field is required and used for authentication.
# first_name: The user's first name.
# last_name: The user's last name.
# email: The user's email address. This field is often used for communication and can also be used for authentication.
# password: The hashed password of the user. This field is automatically managed by Django's authentication system.
# groups: A Many-to-Many relationship to the Group model. Groups can be used to assign permissions to users.
# user_permissions: A Many-to-Many relationship to the Permission model. User permissions grant specific actions or access rights.
# is_staff: A boolean field indicating whether the user has access to the admin site.
# is_active: A boolean field indicating whether the user's account is active. Inactive users cannot log in.
# date_joined: A datetime field that stores the date and time when the user account was created.
# last_login: A datetime field that stores the date and time when the user last logged in.
# is_mfa_active: A boolean field indicating whether the user account has mfa activated or not

    is_mfa_active:bool