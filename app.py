from flask import Flask, render_template, request, redirect, session
from db import database
from  api import API


app = Flask(__name__)

dbo = database()

apo = API()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods =['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = dbo.insert(name,email,password)

    if response == 1:
        return render_template('login.html',message = 'Registration successful, kindly login!')
         
    else:
        return render_template('register.html', message = 'Email already exists')
    
@app.route('/perform_login', methods =['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = dbo.search(email,password)
    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html',message = "Incorrect credentials")

@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')


@app.route('/ner')
def ner():
     if session:
         return render_template('ner.html')
     else:
         return redirect('/')

@app.route('/perform_ner', methods = ['post'])
def perform_ner():

    if session:
        text = request.form.get('ner_text')
        response = apo.ner_analysis(text)
        print(response)
        result = ''
        for i in response['entities']:
            result = result + i['name'] + ' '+ i['category'] + "\n"
        return render_template('ner.html', result = result)
    else:
        return redirect('/')


app.run(debug = True)

