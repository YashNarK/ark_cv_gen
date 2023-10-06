from django.apps import AppConfig
# different user sign in methods:
# 1) username + password + mobile otp => mobile_otp_auth
# 2) username + password + email otp => email_otp_auth
# 3) email + password + mobile otp => email_mobile_otp_auth
# 4) email + password + email otp => 2_email_otp_auth
# 5) WEB3 Signin => web3_auth
# 6) OAuth Sign in (token) => oauth
# 7) username + password + authenticator => authenticator_auth
# 8) email + password + authenticator => email_authenticator_auth

class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
