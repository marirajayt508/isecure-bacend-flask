import json
import math, random
import Modules.Encryption.Enmachine as Encryptor
import Modules.Decryption.Demachine as Decryptor
import Modules.KeySecurity.isecure as isecure
import Modules.mail.mailer as mailer
import Modules.Otp.otp as otp
import Modules.QrLogin.session as login
import Modules.Otp.captha as cap
import DB.db_basic_module.insert as insert
import DB.db_basic_module.check as check
import DB.db_basic_module.user_reg_check as users
import DB.db_basic_module.getkey as keys
import DB.db_basic_module.get_user_info as user_info
import DB.db_basic_module.loginsession as login_sess

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
    
def otps(n):
      digits = "0123456789"
      OTP = ""
      for i in range(n):
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
    
def check_name(name) :
    return users.Namecheck(name)
    
def get_key(key) :
    return keys.getkey(key)
    
def capthas() :
    return cap.captha()
    
def session_active(key,code,otp):
    return login.session(key,code,otp)
    
def session_check(key):
    return login.check_session(key)
    
def session_mail(key):
    return login.get_session(key)
 
def session_name(key):
    return login.get_name(key) 
    
def session_otp(key):
    return login.get_code(key)
    
def session_key(code) :
    return login.get_session_key(code)
    
def session_time(code) :
    return login.get_session_time(code)
    
def session_deactive(key):
    return login.del_session(key)
    
def numcheck(a,b) :
    if a is b :
       return False
    else :
       return True

def user_info_get(key):
    return user_info.Fetch_User_Info(key)

def login_info(datas):
    return login_sess.login_sessiondata(datas)
    
def login_data_validate(key):
    return login_sess.login_get_sessiondata_validate_info(key)
    
def login_data(key):
    return login_sess.login_get_sessiondata(key)
    
def login_data_navi(key):
    return login_sess.login_get_sessiondata_navi(key)
    