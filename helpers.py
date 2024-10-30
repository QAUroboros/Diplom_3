import faker
import random


def get_faker_user() -> dict:
    fake = faker.Faker()
    email = fake.email()
    password = fake.password(length=15, special_chars=True, digits=True, upper_case=True, lower_case=True)
    name = fake.name()
    return {"email": email, "password": password, "name": name}


def generate_registration_data():
    return {
        "name": "Артём",
        "email": f"ArtemKrivoshein13{random.randint(100, 999)}@yandex.ru",
        "password": "123456"
    }
