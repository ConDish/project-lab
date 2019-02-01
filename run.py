from flask import Flask, request, render_template, redirect, url_for, session

import forms

app = Flask(__name__)
PORT = 8000
DEBUG = True

@app.errorhandler(404)
def not_found(error):
   return "Not Found."

@app.route('/', methods=['GET'])
def index():
   

   return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registrar():

   register = forms.registro(request.form)

   return render_template('registro.html', registre = register)



if __name__ == '__main__':
   app.run(port = PORT, debug = DEBUG )