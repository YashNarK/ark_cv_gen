from django.db import models
from django.contrib.auth.models import AbstractUser

class SocialMediaAccount(models.Model):
    # platform: Social media platform of the user
    # username: username of the user in the platform
    SOCIAL_MEDIA_CHOICES = [
        ('LinkedIn','LinkedIn'),
        ('GitHub','GitHub')
    ]
    platform = models.CharField(max_length=20, choices=SOCIAL_MEDIA_CHOICES)
    username = models.CharField(max_length=100)




class CustomUser(   AbstractUser):
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

# CUSTOM FIELDS:
# is_2fa_enabled: A boolean field indicating whether the user account has 2fa activated or not
# is_mobile_verified: A boolean field indicating whether the mobile number has been verified.
# mobile_otp: Store temporary OTPs if needed for verification.
# is_email_verified: A boolean field indicating whether the email address has been verified.
# email_otp: Store temporary OTPs if needed for verification.
# web3_address: The user's Web3 (e.g., Ethereum or polygon) address.
# oauth_token: Store OAuth tokens obtained during sign-in through OAuth providers.
# authenticator_secret: Store secrets for time-based one-time password (TOTP) authentication.
# profile_picture: The user's profile picture URL or reference.
# bio: A brief user bio or description.
# sign_in_types_available: user level control for what type of sign in's available for a user
# links_to_social_profiles: Store links to the user's social media profiles or websites.


    def default_sign_in_types():
        return {
        'mobile_otp_auth': False,
        'email_otp_auth': False,
        'email_mobile_otp_auth': False,
        '2_email_otp_auth': False,
        'web3_auth': False,
        'oauth': False,
        'authenticator_auth': False,
        'email_authenticator_auth': False
    }

    


    # App specific - Custom Fields
    is_2fa_enabled = models.BooleanField(default=False)
    is_mobile_verified = models.BooleanField(default=False)
    mobile_otp = models.CharField(max_length=6, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    email_otp = models.CharField(max_length=6, null=True, blank=True)
    web3_address = models.CharField(max_length=100, null=True, blank=True)
    oauth_token = models.TextField(null=True, blank=True)
    authenticator_secret = models.CharField(max_length=16, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    sign_in_types_available = models.JSONField(default=default_sign_in_types)
    links_to_social_profiles = models.ManyToManyField(
        SocialMediaAccount,
        blank=True,  # Allows for an empty list of profiles
        related_name='linked_users',  # Optionally, you can set a related name
    )


