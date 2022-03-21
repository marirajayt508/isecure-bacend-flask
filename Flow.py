import json
import Modules.Encryption.Enmachine as Encryptor
import Modules.Decryption.Demachine as Decryptor

def Index () :
    return "This is Index page"

def Encryption (data) :
    level1_key,level1_endata=Encryptor.machine(data)
    level2_key,level2_endata=Encryptor.machine(str(level1_endata))
    level3_key,level3_endata=Encryptor.machine(str(level2_endata))
    Encryption = {
       'Encrypted_datas' : {
            'keys' : {
        'key1' : level1_key.decode('ascii'),
        'key2' : level2_key.decode('ascii'),
        'key3' : level3_key.decode('ascii')
        },
        'Other_datas' : {
             'data1' : level1_endata.decode('ascii'),
             'data2' : level2_endata.decode('ascii'),
             'data3' : level3_endata.decode('ascii')
        },
        'data' : level3_endata.decode('ascii')
        }
     }
    return json.dumps(Encryption)

def Decryption (key1,key2,key3,endata) :
    #data=Decryptor.machine(key,endata)
    #level3_data=Decryptor.machine(key3,endata)
    level3_data=Decryptor.machine(key3,endata)

    level2_data=Decryptor.machine(key2, level3_data[2:-1])

    level1_data=Decryptor.machine(key1,level2_data[2:-1])

    Decryption = {'data' : level1_data}
    return json.dumps(Decryption)