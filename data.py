import random

BASE_URL = "https://stellarburgers.nomoreparties.site/"


def generate_registration_data():
    return {
        "name": "Артём",
        "email": f"ArtemKrivoshein13{random.randint(100, 999)}@yandex.ru",
        "password": "123456"
    }
