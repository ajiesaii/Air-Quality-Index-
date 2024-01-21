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
        "apiKey": "",
        "authDomain": "",
        "databaseURL": "",
        "projectId": "",
        "storageBucket": "",
        "messagingSenderId": "",
        "appId": ""
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
