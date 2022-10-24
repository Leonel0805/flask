from wtforms import Form
from wtforms import StringField, TextAreaField, EmailField, PasswordField 
from wtforms import validators


class CreateForm(Form):
    username = StringField("username", [validators.DataRequired()])
    password = PasswordField("contraseña", [validators.DataRequired()])
    email = EmailField("correo electronico", [validators.DataRequired()])
    coment = TextAreaField("comentario")
    