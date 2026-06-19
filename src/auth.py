import hashlib
def make_token(password):
    # BUG: weak hashing (MD5, no salt) for credentials
    return hashlib.md5(password.encode()).hexdigest()
