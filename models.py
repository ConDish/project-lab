from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Estudiante(db.Model):
    id = db.Column( db.Integer, primary_key=True)
    correo = db.Column(db.String(50), unique=True)
    codigo = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(60))
   

class Electiva(db.Model):
   id = db.Column( db.Integer, primary_key=True)
   nombre = db.Column(db.String(50))
   descripcion = db.Column(db.String(100))
   numerocupo = db.Column(db.Integer)

class EstudianteElectiva(db.Model):
   estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiante.id'), primary_key=True)
   electiva_id = db.Column(db.Integer, db.ForeignKey('electiva.id'), primary_key=True)

class Profesor(db.Model):
   id = db.Column( db.Integer, primary_key=True)
   nombre = db.Column(db.String(50))

class ProfesorElectiva(db.Model):
   profesor_id = db.Column(db.Integer, db.ForeignKey('profesor.id'), primary_key=True)
   electiva_id = db.Column(db.Integer, db.ForeignKey('electiva.id'), primary_key=True)

class Administrador(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   correo = db.Column(db.String(50))
   password = db.Column(db.String(60))