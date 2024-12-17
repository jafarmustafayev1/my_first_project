from fields import CharField, PhoneNumberField, PasswordField, EmailField, DateOfBirthField
from commit import commit

class User:
    username = CharField()
    phone = PhoneNumberField()
    password = PasswordField()
    email = EmailField()
    dob = DateOfBirthField()

    def __init__(self, username, phone, password, email, dob):
        self.username = username
        self.phone = phone
        self.password = password
        self.email = email
        self.dob = dob

    @commit
    def save(self):
        print(f"Saving user {self.username}...")

    @commit
    def update(self, username=None, phone=None, password=None, email=None, dob=None):
        if username:
            self.username = username
        if phone:
            self.phone = phone
        if password:
            self.password = password
        if email:
            self.email = email
        if dob:
            self.dob = dob
        print(f"Updated user {self.username}...")

    @commit
    def delete(self):
        print(f"Deleting user {self.username}...")