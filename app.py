from models import User

def test_user_creation():
    try:
        user = User("user1", "+1234567890", "password123", "user1@example.com", "2000-05-15")
        print(f"Username: {user.username}")
        print(f"Phone: {user.phone}")
        print(f"Password: {user.password}")
        print(f"Email: {user.email}")
        print(f"Date of Birth: {user.dob}")
        user.save()
    except ValueError as e:
        print(e)

    try:
        user.update(username="new_user", phone="+123456789012", password="newpassword123")
        print(f"Updated Username: {user.username}")
        print(f"Updated Phone: {user.phone}")
        user.save()
    except ValueError as e:
        print(e)

    try:
        user.delete()
    except ValueError as e:
        print(e)

def test_invalid_user_creation():
    try:
        user = User("user2", "+1234567890", "password123", "invalid-email", "2000-05-15")
        user.save()
    except ValueError as e:
        print(e)

    try:
        user = User("user3", "+1234567890", "password123", "user3@example.com", "2010-05-15")
        user.save()  # Bu xato bo'ladi
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    test_user_creation()
    test_invalid_user_creation()
