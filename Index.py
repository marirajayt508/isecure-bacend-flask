from flask import Flask
app = Flask(__name__)
import Flow 

@app.route('/')
def Index():
    return Flow.Index()

@app.route('/Encryption')
def Encryption():
    return Flow.Encryption("This G.A.S Stote")

@app.route('/Decryption')
def Decryption():
    encrypted = {"Encrypted_datas": {"keys": {"key1": "utfpbb6FIHhsvP_gBtcDwW_prPybgk2msM2SNt3l4BE=", "key2": "0j1C8eXOeX9HkuxF_fqW3xTkGWsRrjCX5MiwdZgflnw=", "key3": "adFQDn0V6bpiwQjt-ulV9bXgIHdM4v5LOL3YwLiy1eU="}, "Other_datas": {"data1": "gAAAAABiODgI1luofa1fGOuceKVdZDcjlUoRSN9OjS9Th16TuT0itOdaehb1MIqsvukMdAJgbQ2d0PiO4yNF5dcyIYgN9jgbDcDFIfI1rtU82dWLIo3yLHY=", "data2": "gAAAAABiODgIQVkhEPX2Iptl3nCJ1v9SBD0VSk4ryb7Ow7d-yLqT51j5r0D4Q9j4eoIsZRbvk46E1LhZAgcH1R_jMXaHsPjm5RAcC0ho-w_9ZuoN5jf1If275Ay2kqunxo6srTvHXPPuXhjvIG3UNM6nZmd7pGJ0N78140sUzUxIZmwSoB3g6EWLE5vY8rmcKlacvAlgKBdFd6FOPO8qbUsC-DkAYhdBW7rt_3HXdw9lZe--EVM8yfg=", "data3": "gAAAAABiODgIVj3iIQABRQgyy99RrDuSN62jVtSN32lvnKndJ_GvriZzEAlo9lvItSnh8MIZL_HSpzqKX8viRxodAR5heEC9wmRn5YsTeVmwC5VqWn4_BooWCvHpJin-Sz_2qQJsn5agmmoEDW1GfwDGqdjqvakFU9A7U7_bhP45cfYyJMmysGBSeVki2GJE4KC_xjbip4gpyRn0VDL2qOdW3Z4h7lg0jACKc48wtnQVXfjI7JaBCfyA3DIvlXwukvEljSrpmdxbu6n9SMKWH6MDS2XlnH8k0nmK4pnzUxNEA1TP3TIft7wDpKL8JeKcQ-dcdqRL3VeMHHmRJOo238XiuBrGtJrOVybKqFLsGTStNCSbnUqpTeRDwnrwFmN78LcDoY1ZoJQUjk4rPle0rQbd2-svAbxkwg=="}, "isecure": {"key1": "utfpbb6FIHhsvP_gBtcDwW_prPybgk2msM2SNt3l4BE=", "key2": "0j1C8eXOeX9HkuxF_fqW3xTkGWsRrjCX5MiwdZgflnw=", "key3": "adFQDn0V6bpiwQjt-ulV9bXgIHdM4v5LOL3YwLiy1eU="}, "data": "gAAAAABiODgIVj3iIQABRQgyy99RrDuSN62jVtSN32lvnKndJ_GvriZzEAlo9lvItSnh8MIZL_HSpzqKX8viRxodAR5heEC9wmRn5YsTeVmwC5VqWn4_BooWCvHpJin-Sz_2qQJsn5agmmoEDW1GfwDGqdjqvakFU9A7U7_bhP45cfYyJMmysGBSeVki2GJE4KC_xjbip4gpyRn0VDL2qOdW3Z4h7lg0jACKc48wtnQVXfjI7JaBCfyA3DIvlXwukvEljSrpmdxbu6n9SMKWH6MDS2XlnH8k0nmK4pnzUxNEA1TP3TIft7wDpKL8JeKcQ-dcdqRL3VeMHHmRJOo238XiuBrGtJrOVybKqFLsGTStNCSbnUqpTeRDwnrwFmN78LcDoY1ZoJQUjk4rPle0rQbd2-svAbxkwg=="}}
    #content = request.json
    #print(content['mytext'])
    #return jsonify({"uuid":uuid})
    key1 = encrypted['Encrypted_datas']['keys']['key1']
    key2 = encrypted['Encrypted_datas']['keys']['key2']
    key3 = encrypted['Encrypted_datas']['keys']['key3']
    endata = encrypted['Encrypted_datas']['data']
    return Flow.Decryption(key1,key2,key3,endata)
    
if __name__ == "__main__" :
      app.run()