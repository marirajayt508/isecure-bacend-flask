import pymongo

from datetime import datetime


myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb")

mydb = myclient["PrdConfig"]

qr_session = mydb["QrSession"]

user_session = mydb["UserDetails"]

now = datetime.now()

def session(key,code,otp) :
    
    sess = {'key' : key, 'code' : code , 'otp' : otp , 'time' : now.strftime("%H:%M:%S"), 'login' : False}
    
    qr_session.insert_one(sess)
    
    print("Session Active")
    
    return "Session Active"
    
def check_session(key):
    
    keys = qr_session.find()

    for i in keys :
    
       if i['code'] == key :
       
           return True
           
       else :
       
           return False
           
def get_session(key):
    
    users = user_session.find()

    for i in users :
    
       if i['key'] == key :
       
           return i['email']
           
       else :
       
           return key
           
def get_name(key):
    
    users = user_session.find()

    for i in users :
    
       if i['key'] == key :
       
           return i['name']
           
       else :
       
           return key
           
def get_session_key(code):
    
    users = qr_session.find()

    for i in users :
    
       if i['code'] == code :
       
           return i['key']
           
       else :
       
           return code

def get_session_time(code):
    
    users = qr_session.find()

    for i in users :
    
       if i['key'] == code :
       
           return i['time']
           
       else :
       
           return code
           
def get_code(key):
    
    users = qr_session.find()

    for i in users :
    
       if i['code'] == key :

           return i['otp']
           
       else :
       
           return key
    
def del_session(key):
    
    qr_session.delete_many(key)
    
    print("Session Deactive")
    
    return "Session End Successfully."