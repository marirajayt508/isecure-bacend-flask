import json
import math, random
import Modules.Encryption.Enmachine as Encryptor
import Modules.Decryption.Demachine as Decryptor
import Modules.KeySecurity.isecure as isecure
import Modules.mail.mailer as mailer
import Modules.Otp.otp as otp
import DB.db_basic_module.insert as insert
import DB.db_basic_module.check as check
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
            'key3' : level3_key.decode('ascii'),
        },
        'Other_datas' : {
             'data1' : level1_endata.decode('ascii'),
             'data2' : level2_endata.decode('ascii'),
             'data3' : level3_endata.decode('ascii')
        },
        'isecure' : {
        'key1':isecure.machineencrypt(level1_endata.decode('ascii').encode('ascii')),
        'key2':isecure.machineencrypt(level2_endata.decode('ascii').encode('ascii')),
        'key3':isecure.machineencrypt(level3_endata.decode('ascii').encode('ascii')),
            'key1' : level1_key.decode('ascii'),
            'key2' : level2_key.decode('ascii'),
            'key3' : level3_key.decode('ascii'),
        },
        'data' : level3_endata.decode('ascii')
        }
     }
    return json.dumps(Encryption)
    
def otps():
      digits = "0123456789"
      OTP = ""
      for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
      return OTP

def otpmailer(email,otp):
    mailer.otpmail(email,otp)
   
def keypassmailer(tomail,keypass):
    mailer.keypassmail(tomail,str(keypass))

def Decryption (key1,key2,key3,endata) :
    #data=Decryptor.machine(key,endata)
    #level3_data=Decryptor.machine(key3,endata)
    #decrypt_isuecue_key3 = isecure.machinedecrypt(key3)
    level3_data=Decryptor.machine(key3,endata)
    #decrypt_isuecue_key2 = isecure.machinedecrypt(key2)
    level2_data=Decryptor.machine(key2, level3_data[2:-1])
    #decrypt_isuecue_key1 = isecure.machinedecrypt(key1)
    level1_data=Decryptor.machine(key1,level2_data[2:-1])


    Decryption = {'data' : level1_data}
    return json.dumps(Decryption)

def BasicInsert(name,password,key):
    insert.Basicdetails(name,password,key)

def KeyInsert(key):
    insert.Keydetails(key)

def UserInsert(name,firstname,lastname,code,phno,email,password,key):
    insert.Userdetails(name,firstname,lastname,code,phno,email,password,key)

def check_key(key) :
    return check.check_keys(key)