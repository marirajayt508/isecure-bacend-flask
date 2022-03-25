import DB.db_basic_module.connection as connection
import Modules.KeySecurity.isecure as keysecure

UserDetails = connection.userdb()

def Namecheck(query) :
        
       count = 0
       for i in UserDetails.find(query) :
            count = count + 1
       return count
