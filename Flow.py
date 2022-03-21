import json
import Modules.Encryption.Enmachine as Encryptor
import Modules.Decryption.Demachine as Decryptor

def Index () :
    return "This is Index page"

def Encryption (data) :
    key,endata=Encryptor.machine(data)
    Encryption = {'key' : key.decode('ascii'), 'data' : endata.decode('ascii')}
    return json.dumps(Encryption)

def Decryption (key,endata) :
    data=Decryptor.machine(key,endata)
    Decryption = {'data' : str(data)}
    return json.dumps(Decryption)