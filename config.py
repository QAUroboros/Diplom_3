from enum import Enum
from data.data import BASE_URL, generate_registration_data


DOMAIN = BASE_URL


class URL(str, Enum):
    SIGN_IN = f'{DOMAIN}login'
    FORGOT_PASSWORD = f'{DOMAIN}forgot-password'
    PASSWORD_CHANGE = f'{DOMAIN}reset-password'
    SIGN_UP = f'{DOMAIN}register'
    USER_PROFILE = f'{DOMAIN}account/profile'
    ORDER_STREAM = f'{DOMAIN}feed'


user_data = generate_registration_data()
LOGIN_USER = user_data["email"]
LOGIN_PASSWORD = user_data["password"]
