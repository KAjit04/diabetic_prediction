# install flask

from flask import Flask, render_template, request
import joblib

# load the model
model = joblib.load('predict_02.pkl')

#initialize the app
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home1.html')

@app.route('/contacts')
def contact():
    return render_template('home.html')

@app.route('/dsa')
def dsa():
    return 'Welcome to dsa page'

@ app.route('/forms')
def forms():
    return render_template('forms.html')

@ app.route('/predict', methods=['post'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age =  request.form.get('age')


    data = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])
    if data[0]==0:
        resp = 'not diabetic'
    else:
        resp = 'diabetic'

    return 'form submitted'


# running the app - this should be at the end of the app
app.run(debug=True)