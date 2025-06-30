from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcript"], deprecated = "auto")

def hash_password(pwd):
    return pwd_context.hash(pwd)

def verify_password(plain_pwd, hash_pwd):
    return pwd_context.verify(plain_pwd, hash_pwd)

