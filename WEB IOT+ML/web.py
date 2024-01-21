from flask import Flask
from flask import render_template
import numpy as np
import pickle
import pyrebase


app = Flask(__name__)

@app.route('/')
def main():
    #inisialisasi firebase
    firebaseConfig = {
        "apiKey": "AIzaSyAyPNnALVGV7jVHocJhdV4lmFP_UNi8c9c",
        "authDomain": "iot-and-ml-7ae55.firebaseapp.com",
        "databaseURL": "https://iot-and-ml-7ae55-default-rtdb.firebaseio.com",
        "projectId": "iot-and-ml-7ae55",
        "storageBucket": "iot-and-ml-7ae55.appspot.com",
        "messagingSenderId": "512631888265",
        "appId": "1:512631888265:web:6b2884401929a5fa4da958"
}

    firebase = pyrebase.initialize_app(firebaseConfig)
    database = firebase.database()
    
    #load model machine learning
    model = pickle.load(open('base/ml.pkl', 'rb'))

    #get data dari firebase
    co = database.child('CO').get().val()
    co2 = database.child('CO2').get().val()
    inputData = [co,co2]                    #inputan untuk ke model
    features = [np.array(inputData)]
    prediction = model.predict(features)    #prediksi
    output = prediction
    print("Hasil prediksi adalah", output)
    print(inputData)
    if output == [0]:                           #apabila hasil prediksi 0 = baik, 1 = buruk, 2 = toxic
        return render_template('baik.html')
    if output == [1]:
        return render_template('buruk.html')
    else:
        return render_template('toxic.html')

if __name__ == '__main__':
    app.run(debug=True)