from flask import Flask,jsonify, request, session, redirect, render_template
from localStoragePy import localStoragePy
from flask_session import Session
from flask_cors import CORS
import random
app = Flask(__name__)
import Flow

status = "false"

@app.route('/',methods = ['POST','GET'])
def Index():
    return jsonify({'msg' : "success"})

@app.route('/ping',methods = ['POST','GET'])
def ping():
    data = request.get_json()
    return data

@app.route('/Register',methods = ['POST','GET'])
def Register():
    data = request.get_json()
    Flow.keypassmailer(data['email'],Flow.Encryption(data['key']))
    return Flow.Encryption(data['key'])
    
@app.route('/Getkey',methods = ['POST','GET'])
def getkey():
    data = request.get_json()
    return Flow.get_key(data['email'])
    
#Start Session
@app.route('/StartSession',methods = ['POST','GET'])
def Sessionstart ():
    data = request.get_json()
    
    qrcode = Flow.capthas()
    
    check = Flow.session_active(data['key'],qrcode,Flow.otps(2))
    
    return jsonify({'qr' : qrcode , 'status' : check})
    
    
#Check Session
@app.route('/CheckSession',methods = ['POST','GET'])
def Sessioncheck():
    data = request.get_json()
    return str(Flow.session_check(data['key']))
    
#End Session
@app.route('/EndSession',methods = ['POST','GET'])
def Sessionend():
    data = request.get_json()
    return str(Flow.session_deactive(data))
    
#MobApp Check Session
@app.route('/AppCheckSession',methods = ['POST','GET'])
def Appsessioncheck():
    data = request.form['key']
    #return str(Flow.session_check(data['key']))
    return jsonify({'msg' : str(Flow.session_check(data))})
 
#MobApp Send Email 
@app.route('/AppSendEmailCode',methods = ['POST','GET'])
def Appsendemail():

    data = request.form['key']
    
    key = str(Flow.session_key(data))
    
    mail =str(Flow.session_mail(key))
    
    name = str(Flow.session_name(key))
    
    otp = str(Flow.session_otp(data))
    
    time = str(Flow.session_time(key))
    
    Flow.otpmailer(mail,otp)
    
    return jsonify({'msg' : "Success", 'time' : time, 'name' : name, 'otp' : otp})
    
#MobApp Choose Session
@app.route('/AppChooseSessionOtp',methods = ['POST','GET'])
def Appsessionchoose():
    data = request.form['code']
    otp_random = [Flow.otps(2),Flow.otps(2),Flow.session_otp(data)]
    class_random = ["btn btn-secondary","btn btn-success","btn btn-warning"]
    num = [0,1,2]
    otp1 = random.choice(num)
    
    chs = random.randrange(2)
    
    if chs == 0 :
       if otp1 in num :
          num.remove(otp1) 

       otp2 = num[0]   
    
       if otp2 in num :
          num.remove(otp2)
       
       otp3 = num[0] 
    
    else :
       if otp1 in num :
          num.remove(otp1) 

       otp2 = num[0]   
    
       if otp2 in num :
          num.remove(otp2)
       
       otp3 = num[0]     

    return jsonify({'otp1' : {'otp_code':otp_random[otp1],'otp_class' : class_random[otp1]},'otp2' :{'otp_code':otp_random[otp2],'otp_class' : class_random[otp2]},'otp3' : {'otp_code':otp_random[otp3],'otp_class' : class_random[otp3]}})

#MobApp Ocode
@app.route('/Ocode',methods = ['POST','GET'])
def Appcheckocode():
    data = request.form['status']
    code = request.form['code']
    device = request.form['device']
    time = request.form['time']
    key = str(Flow.session_key(code))
    user_info = Flow.user_info_get(key)
    if data == "True":
       
       udata = {
       'key' : key,
       'user_datas' : user_info,
       'time' : time,
       'device' : device,
       'LoginStatus' : "true"
       }
       
       Flow.login_info(udata)
       
       status = "true"
   
       return data
    else :
       
       status = "false"
       
       print (status)
   
       return data

@app.route('/Otp',methods = ['POST','GET'])
def otp():
    data = request.get_json()
    otp_val = Flow.otps(6)
    Flow.otpmailer(data['email'],otp_val)
    return otp_val
    
@app.route('/LoginCheck',methods = ['POST','GET'])  
def Logincheck():
    data = request.get_json()
    user_obj = Flow.login_data(data['key'])
    user_obj_test = Flow.login_data_validate(data['key'])
    if user_obj_test :
   
        send_obj = {
            'key' : user_obj['key'],
            'name' : user_obj['user_datas']['name'],
            'firstname' : user_obj['user_datas']['firstname'],
            'lastname' : user_obj['user_datas']['lastname'],
            'code' : user_obj['user_datas']['code'],
            'phonenumber' : user_obj['user_datas']['phonenumber'],
            'email' : user_obj['user_datas']['email'],
            'password' : user_obj['user_datas']['password'],
            'time' : user_obj['time'],
            'device' : user_obj['device'],
            'loginstatus': user_obj['LoginStatus'] 
        }

    else :
    
       send_obj = {
       'loginstatus': 'false' 
       }
    

    return send_obj
 
@app.route('/LoginCheckNavi',methods = ['POST','GET'])  
def Loginchecknavi():
    data = request.get_json()
    user_obj = Flow.login_data_validate(data['key'])
   
    if user_obj :
       return jsonify({'status' : "true"})
    else :
 
       return jsonify({'status' : "true"})
     
 
 
@app.route('/Encryption',methods = ['POST','GET'])
def Encryption():
    data = request.get_json()
    #return jsonify({'data':data['key']})
    return Flow.Encryption(data['key'])
  
@app.route('/Check',methods = ['POST','GET'])  
def Name_check():
    data = request.get_json()
    #return jsonify({'data':data['key']})
    if Flow.check_name(data) :
        msg = "false"
    else :
        msg = "true"
    
    return msg
    
@app.route('/Captha',methods = ['POST','GET'])  
def captha():
    data = request.get_json()
    #return jsonify({'data':data['key']})
 
    return Flow.capthas()
  
@app.route('/KeyCheck',methods = ['POST','GET'])   
def Keycheck():
    data = request.get_json()
    
    return str(Flow.check_key(data['key']))


@app.route('/Decryption',methods = ['POST','GET'])
def Decryption():
    #encrypted = {"Encrypted_datas": {"keys": {"key1": "utfpbb6FIHhsvP_gBtcDwW_prPybgk2msM2SNt3l4BE=", "key2": "0j1C8eXOeX9HkuxF_fqW3xTkGWsRrjCX5MiwdZgflnw=", "key3": "adFQDn0V6bpiwQjt-ulV9bXgIHdM4v5LOL3YwLiy1eU="}, "Other_datas": {"data1": "gAAAAABiODgI1luofa1fGOuceKVdZDcjlUoRSN9OjS9Th16TuT0itOdaehb1MIqsvukMdAJgbQ2d0PiO4yNF5dcyIYgN9jgbDcDFIfI1rtU82dWLIo3yLHY=", "data2": "gAAAAABiODgIQVkhEPX2Iptl3nCJ1v9SBD0VSk4ryb7Ow7d-yLqT51j5r0D4Q9j4eoIsZRbvk46E1LhZAgcH1R_jMXaHsPjm5RAcC0ho-w_9ZuoN5jf1If275Ay2kqunxo6srTvHXPPuXhjvIG3UNM6nZmd7pGJ0N78140sUzUxIZmwSoB3g6EWLE5vY8rmcKlacvAlgKBdFd6FOPO8qbUsC-DkAYhdBW7rt_3HXdw9lZe--EVM8yfg=", "data3": "gAAAAABiODgIVj3iIQABRQgyy99RrDuSN62jVtSN32lvnKndJ_GvriZzEAlo9lvItSnh8MIZL_HSpzqKX8viRxodAR5heEC9wmRn5YsTeVmwC5VqWn4_BooWCvHpJin-Sz_2qQJsn5agmmoEDW1GfwDGqdjqvakFU9A7U7_bhP45cfYyJMmysGBSeVki2GJE4KC_xjbip4gpyRn0VDL2qOdW3Z4h7lg0jACKc48wtnQVXfjI7JaBCfyA3DIvlXwukvEljSrpmdxbu6n9SMKWH6MDS2XlnH8k0nmK4pnzUxNEA1TP3TIft7wDpKL8JeKcQ-dcdqRL3VeMHHmRJOo238XiuBrGtJrOVybKqFLsGTStNCSbnUqpTeRDwnrwFmN78LcDoY1ZoJQUjk4rPle0rQbd2-svAbxkwg=="}, "isecure": {"key1": "utfpbb6FIHhsvP_gBtcDwW_prPybgk2msM2SNt3l4BE=", "key2": "0j1C8eXOeX9HkuxF_fqW3xTkGWsRrjCX5MiwdZgflnw=", "key3": "adFQDn0V6bpiwQjt-ulV9bXgIHdM4v5LOL3YwLiy1eU="}, "data": "gAAAAABiODgIVj3iIQABRQgyy99RrDuSN62jVtSN32lvnKndJ_GvriZzEAlo9lvItSnh8MIZL_HSpzqKX8viRxodAR5heEC9wmRn5YsTeVmwC5VqWn4_BooWCvHpJin-Sz_2qQJsn5agmmoEDW1GfwDGqdjqvakFU9A7U7_bhP45cfYyJMmysGBSeVki2GJE4KC_xjbip4gpyRn0VDL2qOdW3Z4h7lg0jACKc48wtnQVXfjI7JaBCfyA3DIvlXwukvEljSrpmdxbu6n9SMKWH6MDS2XlnH8k0nmK4pnzUxNEA1TP3TIft7wDpKL8JeKcQ-dcdqRL3VeMHHmRJOo238XiuBrGtJrOVybKqFLsGTStNCSbnUqpTeRDwnrwFmN78LcDoY1ZoJQUjk4rPle0rQbd2-svAbxkwg=="}}
    encrypted = request.get_json()
    #print(content['mytext']) 'Encrypted_datas' : {
    #return jsonify({"uuid":uuid})
    key1 = encrypted['Encrypted_datas']['keys']['key1']
    key2 = encrypted['Encrypted_datas']['keys']['key2']
    key3 = encrypted['Encrypted_datas']['keys']['key3']
    endata = encrypted['Encrypted_datas']['data']
    return Flow.Decryption(key1,key2,key3,endata)
    #return Flow.Decryption(key1,key2,key3,endata)

@app.route('/InsertBasicLogin',methods = ['POST','GET'])
def InsertBasicLogin():
    data = request.get_json()
    col = ['BaicDetails','KeyDetails','UserDetails']
    if data['collection'] in col :

        if (data['collection'] == "BaicDetails") : #name,password,key,collection
            Flow.BasicInsert(data['name'],data['password'],data['key'])
            return "Basic Details Inserted"

        elif (data["collection"]=="KeyDetails") :  #key,collection
            if(Flow.check_key(data['key'])):
               return "Ohh Sorry, Data Alredy Exist !!!.."
            else :   
               Flow.KeyInsert(data['key'])
               return "Key Details Inserted"

        elif (data["collection"]=="UserDetails") : #name/firstname,lastname,code,phonenumber
            Flow.UserInsert(data['name'],data['firstname'],data['lastname'],data['code'],data['phonenumber'],data['email'],data['password'],data['key'])
            return "User Details Inserted"
        else:
             return "Collection Not Found" 
        return 1
 
    
if __name__ == "__main__" :
      CORS(app)
      app.config["SESSION_PERMANENT"] = False
      app.config["SESSION_TYPE"] = "filesystem"
      Session(app)
      app.run(host= '192.168.211.37')

'''data = request.get_json()
    col = ['BaicDetails','KeyDetails','UserDetails']
    if data['collection'] in col :

        if (data['collection'] == "BaicDetails") : #name,password,key,collection
            Flow.BasicInsert(data['Name'],data['Password'],data['Key'])
            return "Basic Details Inserted"

        elif (data["collection"]=="KeyDetails") :  #key,collection
            Flow.KeyInsert(data['key'])
            return "Key Details Inserted"

        elif (data["collection"]=="UserDetails") : #name/firstname,lastname,code,phonenumber
            Flow.UserInsert(data['name'],data['firstname'],data['lastname'],data['code'],data['phonenumber'],data['email'],data['password'],data['key'])
            return "User Details Inserted"
        else:'''