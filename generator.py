import secrets
import string


def generate_password():
    password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(16))

    return password
