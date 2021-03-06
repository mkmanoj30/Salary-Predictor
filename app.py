import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('YearsOfExp.mdl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    years_of_exp = float(request.form['yExp'])
  
    prediction = model.predict([[years_of_exp]])

    

    return render_template('index.html', prediction_text='Expected Salary is $ {}'.format(round(prediction[0])))


if __name__ == "__main__":
    app.run(debug=True)