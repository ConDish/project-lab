from flask import Flask, request, render_template, redirect, url_for, session, jsonify
import os
import forms
import json

from models import *

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)

db.init_app(app)

# Session(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://ucumiobsfqvbol:daa1875d1c22ee0373cafe10fea8be9d94b05e247586c6bfedaa3b7d50e9c09f@ec2-23-21-244-254.compute-1.amazonaws.com:5432/dt61msb1aotuf"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.errorhandler(404)
def not_found(error):
   return "Not Found."

@app.route('/', methods=['GET'])
def index():
   if "administrador" in session:
      return render_template('index.html', administrador=session["administrador"])
   elif "usuario" in session:
      return render_template('index.html', usuario=session["usuario"])
   else:
      return render_template('index.html')

# -------------------- REGISTRO ------------------------
@app.route('/registro', methods=['GET', 'POST'])
def registrar():

      register = forms.registro(request.form)


      if request.method == 'POST' :

         try : 
            
            user = json.loads(request.data.decode('utf-8'))


            register = Estudiante(correo=user["correo"], codigo = int(user["cdestudiante"]), password=user["password"])
               
            db.session.add(register)

            db.session.commit()

            session['usuario'] = user["correo"]

            return jsonify({"success" : "1"})
         except:
            return jsonify({"success" : "0"})

      return render_template('registro.html', registre = register)

# -------------------- lOGIN ------------------------           
@app.route('/login', methods=["GET", "POST"])
def login() : 
      login = forms.login(request.form)

      if request.method == 'POST': 

         # user = Estudiante.query.order_by(Estudiante.id).all()
         try :

            user = json.loads(request.data.decode('utf-8'))

            admin = Administrador.query.filter_by(correo=user["correo"], password=user["password"]).first()
            usuario = Estudiante.query.filter_by(correo=user["correo"], password=user["password"]).first()

            if admin is None :
               if usuario is None:
                  return jsonify({'success' : '0'})
               else : 
                  session['usuario'] = user["correo"]
                  return jsonify({'success' : '2'})
            else:
               session['administrador'] = user["correo"]
               return jsonify({'success' : '1'})
         except :
            return jsonify({'success' : '3'})

      if "administrador" in session or "usuario" in session :
         return redirect(url_for('index'))
      else :
         return render_template('login.html', form = login)


# -------------------- ADMINISTRADOR ------------------------
@app.route('/administrador', methods=["GET", "POST"])
def administrador():
   
   if 'administrador' in session:


      return render_template('admin/administrador.html', administrador=session["administrador"])
   else :
      return redirect(url_for('index'))

# ----------------------- PROFESOR ---------------------------------
@app.route('/profesorcrud', methods=["GET", "POST"])
def profesorcrud():

   if 'administrador' in session:

      profesor = forms.profesor(request.form)

      # register = Profesor(nombre="Pepito", electiva_id=3)

      # Todas las electivas 
      elest = db.session.query(Electiva).all()

      proelec = db.session.query(Profesor, Electiva).outerjoin(ProfesorElectiva).outerjoin(Electiva)
               
      # db.session.add(register)

      # db.session.commit()

      if request.method == "POST":
         try :

            profesor = json.loads(request.data.decode('utf-8'))


            register = Profesor(id=int(profesor["codigo"]), nombre=profesor["nombre"])

            db.session.add(register)

            if profesor["electiva_id"] != 0:
               elecpro = ProfesorElectiva(profesor_id=int(profesor["codigo"]), electiva_id=profesor["electiva_id"])

               db.session.add(elecpro)
               
            db.session.commit()


            return jsonify({'success' : '1'})

         except:
            return jsonify({'success': '0'})
      return render_template('admin/profesorcrud.html', administrador=session["administrador"], form = profesor, elest=elest, proelec=proelec)
   else :

      return redirect(url_for('login'))


# --------------------- EDITAR PROFESOR ----------------------------
@app.route("/profesoreditar", methods=["GET", "POST"])
def profesoreditar():

   if 'administrador' in session and request.method == "POST":
      
      try :
            
         profesor = json.loads(request.data.decode('utf-8'))

         proall = Profesor.query.filter_by(id=profesor["idvieja"]).first()
            
         if proall is not None:
               
            elecpro = ProfesorElectiva.query.filter_by(profesor_id=int(profesor["idvieja"])).first()

            if elecpro is not None:

               db.session.delete(elecpro)

               db.session.commit()

               if profesor["electiva_id"] != 0:

                  
                  proall.id = int(profesor["idnueva"])

                  db.session.commit()

                  add = ProfesorElectiva(profesor_id=int(profesor["idnueva"]), electiva_id=int(profesor["electiva_id"]))

                  db.session.add(add)

                  db.session.commit()
                 
               else :

                  proall.id = int(profesor["idnueva"])
                  proall.nombre = profesor["nombre"]

                  db.session.commit()

                  add = ProfesorElectiva(profesor_id=int(profesor["idnueva"]), electiva_id=int(profesor["electiva_id"]))

                  db.session.add(add)

                  db.session.commit()

            return jsonify({'success': '1'})
      except:
         return jsonify({'success' : '0'})
     
   else:
      return redirect(url_for('login'))


# --------------------- ELIMINAR PROFESOR ----------------------------
@app.route('/profesoreliminar/<id>', methods=["GET"])
def profesoreliminar(id):

   if 'administrador' in session:

      if request.method == "GET":
         
         try :

            profesor = db.session.query(Profesor).filter(Profesor.id==id).first()

            db.session.delete(profesor)
            db.session.commit()

            return jsonify({'success' : '1'})

         except Exception:
            return jsonify({'success' : '0'})

      else :
        return jsonify({'success' : '0'})
      
   else :
      return redirect(url_for('login'))



# --------------------- ELECTIVA ----------------------------
@app.route('/electivascrud', methods=["GET", "POST"])
def electivascrud():

   if 'administrador' in session:

      electivas = forms.electivas(request.form)


      # Todas las electivas que tiene estudiantes
      elecpro = db.session.query(Electiva, Estudiante, Profesor).outerjoin(EstudianteElectiva).outerjoin(Estudiante).outerjoin(ProfesorElectiva).outerjoin(Profesor).all()


      # for e,s,p in elecpro:
      #    print(e,s,p)


      # for dato in elest:
      #    print(dato)
      #    test = db.session.query(ProfesorElectiva, Profesor).filter(ProfesorElectiva.electiva_id==dato.id).first()
      #    # est = db.session.query(Estudiante).filter(Estudiante.id==dato.estudiante_id).first()
      #    # elecall.append([dato, pro, est])

      if request.method == "POST":
         try :

            electiva = json.loads(request.data.decode('utf-8'))

            register = Electiva(nombre=electiva["nombre"], descripcion=electiva["descripcion"], numerocupo=electiva["numerocupo"], profesor_id=None, estudiante_id=None)
               
            db.session.add(register)

            db.session.commit()

            return jsonify({'success' : '1'})

         except:
            return jsonify({'success': '0'})

      return render_template('admin/electivascrud.html', administrador=session["administrador"], form = electivas, elecpro=elecpro)
   else :
      return redirect(url_for('login'))

# --------------------- ELIMINAR ELECTIVA ----------------------------
@app.route('/electivaeliminar/<id>', methods=["GET"])
def electivaeliminar(id):

   if 'administrador' in session:

      if request.method == "GET":
         
         try :

            electiva = db.session.query(Electiva).filter(Electiva.id==id).first()

            db.session.delete(electiva)
            db.session.commit()

            return jsonify({'success' : '1'})

         except Exception:
            return jsonify({'success' : '0'})

      else :
        return jsonify({'success' : '0'})
      
   else :
      return redirect(url_for('login'))


# --------------------- EDITAR ELECTIVA  -----------------------------
@app.route("/electivaeditar", methods=["GET", "POST"])
def electvaeditar():

   if 'administrador' in session:
      if request.method == "POST":
         try :
            
            electiva = json.loads(request.data.decode('utf-8'))

            electivall = Electiva.query.filter_by(id=electiva["id"]).first()
            
            if electivall is not None:
               
               electivall.nombre = electiva["nombre"]
               electivall.descripcion = electiva["descripcion"]
               electivall.numerocupo = int(electiva["numerocupo"])
               db.session.commit()

            return jsonify({'success': '1'})
         except:
            return jsonify({'success' : '0'})
     
   else:
      return redirect(url_for('login'))


# -------------------- USUARIO ------------------------
@app.route('/usuario', methods=["GET", "POST"])
def usuario():
   if 'usuario' in session:

      # register = Profesor(nombre="Pepito", electiva_id=3)

      # Todas las electivas 
      elest = db.session.query(Electiva).all()
      estlec = db.session.query(Estudiante, Electiva).outerjoin(EstudianteElectiva).outerjoin(Electiva)

      if request.method == "POST":
         try :

            electiva = json.loads(request.data.decode('utf-8'))
         
            usuario =  Estudiante.query.filter_by(correo=session["usuario"]).first()

            datoelec = Electiva.query.filter_by(id=electiva["electiva_id"]).first()

            datoelec.numerocupo -= 1

            register = EstudianteElectiva(estudiante_id=usuario.id, electiva_id=electiva["electiva_id"])
               
            db.session.add(register)

            db.session.commit()

            return jsonify({'success' : '1'})

         except:
            return jsonify({'success': '0'})

      return render_template('usuario.html', usuario=session["usuario"], estlec=estlec, elest=elest)
   else:
      return redirect(url_for('login'))


# --------------------- CERRAR  SECION ----------------------------
@app.route('/logout/<nombre>', methods=["GET"])
def logout(nombre):

   if nombre in session:
      session.pop(nombre)
      return redirect(url_for('login'))
   else:
      return "No hay session"

if __name__ == '__main__':
   
   db.init_app(app)

   with app.app_context():
      db.create_all()

   app.run(port = 8001, debug = True)