from django.apps import AppConfig
# different user sign in methods:
# 1) username + password + mobile otp
# 2) username + password + email otp
# 3) email + password + mobile otp
# 4) email + password + email otp
# 5) WEB3 Signin
# 6) OAuth Sign in (token)
# 7) username + password + authenticator
# 8) email + password + authenticator

class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
