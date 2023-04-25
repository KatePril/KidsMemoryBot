import hashlib

def make_md5_password(password):
    return hashlib.md5(password.encode()).hexdigest()
