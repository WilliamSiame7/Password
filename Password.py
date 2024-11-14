def is_valid_password(password):
    invalid_chars = '@/()"\'`'
    if len(password) < 15:
        print("Password must have at least 15 characters.")
        return False
    if not password[0].isalpha():
        print("Password must start with a letter.")
        return False
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        return False
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return False
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one number.")
        return False
    if any(char in invalid_chars for char in password):
        print(f"Password must not contain any of these characters: {invalid_chars}")
        return False
    return True

while True:
    password = input("Enter a password: ")
    if is_valid_password(password):
        confirm_password = input("Re-enter the password: ")
        if password == confirm_password:
            print("Password successfully created!")
            break
        else:
            print("Passwords do not match. Try again.")
