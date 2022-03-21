from flask import Flask
app = Flask(__name__)
import Flow 

@app.route('/')
def Index():
    return Flow.Index()

@app.route('/Encryption')
def Encryption():
    return Flow.Encryption("9080122084")

@app.route('/Decryption')
def Decryption():
    encrypted = {"key": "ZMNKsXFfksEUT7_1_rPsm4UU29XCjXan3MvABNEOCcY=", "data": "gAAAAABiOA-BOVxrBVGoWSjmtKe6PCoK_ymVEJ8Mnjowwoh1pzprHDuKjpOADvBfVsj_RMMNrHeT8WPx9YhOvRMe5mNxQj-Vlg=="}
    #content = request.json
    #print(content['mytext'])
    #return jsonify({"uuid":uuid})
    return Flow.Decryption(encrypted['key'],encrypted['data'])
    
if __name__ == "__main__" :
      app.run()