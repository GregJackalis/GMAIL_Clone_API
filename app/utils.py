from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


#function that hashes a password
def hash_password(password):
    return pwd_context.hash(password)

#function that verifies the given password is the same as the password that is hashed
#in order to do that we take the input from the user hash it as well and check if the hashed password are the same
def verify_password(given_password, database_password):
    return pwd_context.verify(given_password, database_password)
