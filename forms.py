from wtforms import Form, TextField, StringField, PasswordField, IntegerField


class registro(Form):
    correo = StringField('Correo')
    cdestudiante = StringField('Codigo de estudiante')
    password = PasswordField('Contrasena')
    confirmpass = PasswordField('Confirmacion de contrasena')

class login(Form):
   correo = StringField('Correo')
   password = StringField('Contrasena')
   

class generarCodigo(Form):
   codigo = IntegerField('Codigo')
   