from django.contrib.auth.models import AbstractUser
import pymongo

class SocialMediaAccount(dict):
    # platform: Social media platform of the user
    # username: username of the user in the platform
    SOCIAL_MEDIA_CHOICES = [
        ('LinkedIn','LinkedIn'),
        ('GitHub','GitHub')
    ]

    def __init__(self, platform, username):
        super().__init__(platform=platform,username=username)




class CustomUser(dict):
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

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
