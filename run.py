from flask import Flask, request, render_template, redirect, url_for, session, jsonify

import forms
import json

from models import db, Estudiante, CodigoEstudiante

app = Flask(__name__)
db.init_app(app)
app.scret_key = "1234567*"

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://kzjokbljcbabsg:6d7ca0101555cedef60d322b2ae72bf0f528ba036445f30f40eec76a65e8996f@ec2-54-243-223-245.compute-1.amazonaws.com:5432/d4smb34a5ue7mu"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.errorhandler(404)
def not_found(error):
   return "Not Found."

@app.route('/', methods=['GET'])
def index():
   return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registrar():

   register = forms.registro(request.form)

   flag = False

   if request.method == 'POST' :
      try : 
         user = {
            "correo" : request.form['correo'],
            "cdestudiante" : request.form['cdestudiante'],
            "password" : request.form['password'],
            "confirmpass" : request.form["confirmpass"]
         }

         register = Estudiante(correo=user["correo"], codigo = user["cdestudiante"], password=user["password"], confirmpass=user["confirmpass"])

         print(register)

         db.session.add(register)
         db.session.commit()

         flag = True

         
      except : 
         flag = False
      finally :

         if flag : 
            return redirect(url_for('index'))
         else :
            return redirect(url_for('registrar'))

         
   return render_template('registro.html', registre = register)

@app.route('/login', methods=["GET", "POST"])
def login() : 

   login = forms.login(request.form)

   if request.method == 'POST': 
      user = {
         "correo" : login.correo.data,
         "password" : login.password.data
      }
      user = Estudiante.query.order_by(Estudiante.id).all()

      print(user)

   return render_template('login.html', form = login)

@app.route('/generarCodigo', methods=["GET", "POST"])
def generarCodigo():

   generarcode = forms.generarCodigo(request.form)



   if request.method == 'POST':

      try : 
         # Sirve para recoger los bytes de la request y convertirlo en utf
         data = json.loads(request.data.decode('utf-8'))

         generarcode = CodigoEstudiante(codigo=int(data["codigo"]), flag=True)

         db.session.add(generarcode)
         db.session.commit()
         
         #print('asdasasd', generarcode[0].id)

         
         return jsonify('{"success" : "1"}')

      except : 

         return jsonify('{"success" : "0"}')


   return render_template('generarCodigo.html', generarCodigo = generarcode)


if __name__ == '__main__':

   with app.app_context():
      db.create_all()
   app.run(port = 5000, debug = False)