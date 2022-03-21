from cryptography.fernet import Fernet
def machine(data) :
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    endata = cipher_suite.encrypt(bytes(data,'ascii'))
    return (key,endata)