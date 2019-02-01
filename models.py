from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Estudiante(db.Model):
    id = db.Column( db.Integer, primary_key=True)
    correo = db.Column(db.String(50))
    codigo = db.Column(db.Integer)
    password = db.Column(db.String(60))
    confirmpass = db.Column(db.String(80))

class Electiva(db.Model):
   id = db.Column( db.Integer, primary_key=True)
   nombre = db.Column(db.String(50))
   descripcion = db.Column(db.String(100))
   numerocupo = db.Column(db.Integer)

class Profesor(db.Model):
   id = db.Column( db.Integer, primary_key=True)
   nombre = db.Column(db.String(50))
   idelectiva = db.Column(db.Integer, db.ForeignKey('electiva.id'))

class CodigoEstudiante(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   codigo = db.Column(db.Integer)
   flag = db.Column(db.Boolean)