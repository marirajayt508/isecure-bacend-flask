import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb")

mydb = myclient["PrdConfig"]

def basicdb():
    return mydb["BasicDetails"]

def keydb():
    return mydb["KeyDetails"]

def userdb():
    return mydb["UserDetails"]



