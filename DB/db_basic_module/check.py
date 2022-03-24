import DB.db_basic_module.connection as connection
import Modules.KeySecurity.isecure as keysecure
#myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb")



KeyDetails = connection.keydb()


def check_keys(key):
    keys = KeyDetails.find()

    for i in keys :
       if i['key'] == key :
           return True
       else :
           return False


#dsaghj34jkhsdfjsh
  