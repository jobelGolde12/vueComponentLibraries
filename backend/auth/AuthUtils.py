import bcrypt
import random

def get_password_hash(password):
    pass_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pass_bytes, salt)
    return hashed_password.decode('utf-8')


def generate_verification_code(length=6):
    return ''.join(random.choice('0123456789') for _ in range(length))
