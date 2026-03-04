from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)
#load saved model
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    area=float(request.form['area'])
    prediction=model.predict(np.array([[area]]))
    return render_template('index.html',prediction_text='Predicted price for area {} is {}'.format(area,prediction[0]))
if __name__=="__main__":
    app.run(host="0.0.0.0",port=10000)