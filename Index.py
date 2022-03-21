from flask import Flask
app = Flask(__name__)
import Flow 

@app.route('/')
def Index():
    return Flow.Index()

@app.route('/Encryption')
def Encryption():
    return Flow.Encryption("Hai This is Mariraja Selvaraja. I am Software Engineer. 9080122084 this is my mobile number. i am a TCS'er ")

@app.route('/Decryption')
def Decryption():
    encrypted = {"Encrypted_datas": {"keys": {"key1": "L_uqEBX1qjMuRyNzcJHk-6VXQtA3HMFCx57v9rJpy1U=", "key2": "26z1XaaSNJm4sMbQ0zm1P11LOABNz-6a8l1JfArtJkc=", "key3": "AoTcCfinGXpxHU2SjG9Rtzn2GU5n45MWUYNmBG_Jvic="}, "Other_datas": {"data1": "gAAAAABiOCEBgWr60poRXpOcN5p-9fUWn5TLJNcfHApv6dM_W69GRStPKgzJmdhV_dEXp3OGffQfqjwBFU93kDroSbWAcRFLR_E9pkivJM3pn7lIMxOD6vJ8fuxbPnxk6whQtLNWLrHLH_ANR9-FxLirTn9us4EcGpjQXb_1I-IOye2YG1Q1DwQ5xYp369As-DC83eq0B64PA598M09bwZlIMDX9f6yeHw==", "data2": "gAAAAABiOCECVVc8G3jSh_oNkUaV3PQ8l85wFtY5SD1tPZFCikU11VlVOGgWoErIj5nHpuUHYqhi_x5MV3A2k0cHcTBFjWVNRpQ2zjPWTi7iysTJ-CDwcR9etjVTzKFcxCg8E7QhF78XJl3tPpm8lYi82_DFhO9eV6jNCiFnhhtOHyOy0yYE72P_Lx13lViLmuo5GBj8sQnPYHdVmNmzCM8NwP9Z3bwIdbE115qWF5N3C_yRoMRa5HG8Nmk89nTLxSMNXOfj0_qFbEnA6MaR36i-LjqwG2PePkx99V0vl6MgHUeaJIKIp3rHcUCZ1_PnWSt7OwL9E14_s442NKdPq-S_d_NpY-gQ6azaWXYQT4ErJP93mqG4mhYiAftKeHV9-FiPl5lIxNZg", "data3": "gAAAAABiOCEC9RvrXhHa0X1C3UcD688r30Id4M9Tm_dhiCdG_2QWA4DYAZaWwPSbR5Die5QM83ZISWEuIq8fLGKahZNpQeTj7MMLQtCKEIN_KJ42OkUzWe3Ql5SO2TIjAYReTbCOlF3RaE0PVzGqE3fit7G0PltrOvkCrve1iK2ALX9675EMYNx9sDpqyNFkRzB7W4dCUbPKBnDuNjb6SJVACznVR3nmjqTS8ltJ10o0pnQStBEcQtPBWw2tPy2NGAn2mMh2AerasOtWDtGaTQfT5e9aBWr0YPL1kd_yUy6O5juJSLMp1z-vZjddh7L15lthQqXdYKyhid8kRO0QArXHxsY8WIWnnrGMDEe0w5EhxsCg4VWSfsJPmLE7rXWpzyDZa4vkUXHJ9uTrW9P1QYkIS82maPD2o_1c173CYv9mXdPfGDvkvnocBtxZEL0VZ3YIAh_yoChC4XK-pY8q2wsqd77tWiL-onwrGFKqxiqK5t4Clj2-PfVh8zwlPH-i6aSod1Lx-7oEnCXkxdGYgp2YPQZZXO3tjGl2bTOWV76wiXYJFjkjOzpzOSsto8smrokVhmPpHQRBFrVSrg73IGNvOusQziZ0qw=="}, "data": "gAAAAABiOCEC9RvrXhHa0X1C3UcD688r30Id4M9Tm_dhiCdG_2QWA4DYAZaWwPSbR5Die5QM83ZISWEuIq8fLGKahZNpQeTj7MMLQtCKEIN_KJ42OkUzWe3Ql5SO2TIjAYReTbCOlF3RaE0PVzGqE3fit7G0PltrOvkCrve1iK2ALX9675EMYNx9sDpqyNFkRzB7W4dCUbPKBnDuNjb6SJVACznVR3nmjqTS8ltJ10o0pnQStBEcQtPBWw2tPy2NGAn2mMh2AerasOtWDtGaTQfT5e9aBWr0YPL1kd_yUy6O5juJSLMp1z-vZjddh7L15lthQqXdYKyhid8kRO0QArXHxsY8WIWnnrGMDEe0w5EhxsCg4VWSfsJPmLE7rXWpzyDZa4vkUXHJ9uTrW9P1QYkIS82maPD2o_1c173CYv9mXdPfGDvkvnocBtxZEL0VZ3YIAh_yoChC4XK-pY8q2wsqd77tWiL-onwrGFKqxiqK5t4Clj2-PfVh8zwlPH-i6aSod1Lx-7oEnCXkxdGYgp2YPQZZXO3tjGl2bTOWV76wiXYJFjkjOzpzOSsto8smrokVhmPpHQRBFrVSrg73IGNvOusQziZ0qw=="}}
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