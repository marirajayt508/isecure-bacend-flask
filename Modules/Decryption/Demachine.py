from cryptography.fernet import Fernet
def machine(key,endata) :
    cipher_suite = Fernet(key)
    data = cipher_suite.decrypt(bytes(endata,'ascii'))
    return data.decode('ascii')