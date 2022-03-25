import DB.db_basic_module.connection as connection
import Modules.KeySecurity.isecure as keysecure

UserDetails = connection.userdb()

def getkey(query):
     
    for i in UserDetails.find(query) :
          key = i['key']
        
    return key