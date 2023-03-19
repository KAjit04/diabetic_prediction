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
    preg = int(request.form.get('preg'))
    plas = int(request.form.get('plas'))
    pres = int(request.form.get('pres'))
    skin = int(request.form.get('skin'))
    test = int(request.form.get('test'))
    mass = int(request.form.get('mass'))
    pedi = int(request.form.get('pedi'))
    age =  int(request.form.get('age'))


    data = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])
    if data[0]==0:
        resp = 'not diabetic'
    else:
        resp = 'diabetic'

    return render_template('forms.html', data = resp)

# running the app - this should be at the end of the app
app.run(debug=True)