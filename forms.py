from wtforms import Form, TextField, StringField, PasswordField, IntegerField, SelectField, TextAreaField


class registro(Form):
    correo = StringField('Correo')
    cdestudiante = StringField('Codigo de estudiante')
    password = PasswordField('Contrasena')
    confirmpass = PasswordField('Confirmacion de contrasena')

class login(Form):
   correo = StringField('Correo')
   password = PasswordField('Contrasena')
   

class generarCodigo(Form):
   codigo = IntegerField('Codigo')

class profesor(Form):
   idprofe = IntegerField('Codigo')
   nombre = StringField('Nombre')

class electivas(Form):
   nombre = StringField('Nombre')
   descripcion = TextAreaField('Descripcion')
   numerocupo = IntegerField('Numero de cupos')
   