import DB.db_basic_module.connection as connections
import Modules.KeySecurity.isecure as keysecure

BaicDetails = connections.basicdb()
KeyDetails = connections.keydb()
UserDetails = connections.userdb()

def Basicdetails(name,password,key):
   Basicdict = { "name": name, "password": password, "key" : key }
   BaicDetails.insert_one(Basicdict)
   print("Basic Details inserted")
   
def Keydetails(key):
   Keydict = { "key" : key }
   KeyDetails.insert_one(Keydict)
   print("Key Details inserted")

def Userdetails(name,firstname,lastname,code,phonenumber,email,password,key):
   userdict = { "name": name, "firstname": firstname, "lastname": lastname, "code": code, "phonenumber": phonenumber, "email": email, "password": password, "key": key }
   UserDetails.insert_one(userdict)
   print("User Details inserted")