from wtforms import Form, TextField, StringField, PasswordField


class registro(Form):
    correo = StringField('Correo')
    cdestudiante = StringField('Codigo de estudiante')
    password = PasswordField('Contrasena')
    confirmpass = PasswordField('Confirmacion de contrasena')