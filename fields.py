import re
from datetime import datetime

class CharField:
    def __get__(self, instance, owner):
        return instance.__dict__.get('_username', '')

    def __set__(self, instance, value):
        if not value:
            raise ValueError("Username can't be empty!")
        instance.__dict__['_username'] = value

class PhoneNumberField:
    def __get__(self, instance, owner):
        return instance.__dict__.get('_phone', '')

    def __set__(self, instance, value):
        if len(value) < 13:
            raise ValueError("Phone number can't be less than 13 digits!")
        instance.__dict__['_phone'] = value

class PasswordField:
    def __get__(self, instance, owner):
        return instance.__dict__.get('_password', '')

    def __set__(self, instance, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long!")
        instance.__dict__['_password'] = value

class EmailField:
    def __get__(self, instance, owner):
        return instance.__dict__.get('_email', '')

    def __set__(self, instance, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid email format!")
        instance.__dict__['_email'] = value

class DateOfBirthField:
    def __get__(self, instance, owner):
        return instance.__dict__.get('_dob', '')

    def __set__(self, instance, value):
        try:
            dob = datetime.strptime(value, "%Y-%m-%d")  # YYYY-MM-DD formatida
            if (datetime.now() - dob).days < 18 * 365:  # 18 yoshdan kichik bo'lishi mumkin emas
                raise ValueError("User must be at least 18 years old!")
            instance.__dict__['_dob'] = value
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
