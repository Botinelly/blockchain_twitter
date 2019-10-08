from flask_wtf import FlaskForm
from datetime import date
from wtforms import StringField, PasswordField, IntegerField, BooleanField, DateField, FileField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    firstName = StringField("firstName", validators = [DataRequired()])
    lastName = StringField("lastName", validators = [DataRequired()])
    

class PostForm(FlaskForm):
    user = StringField("id do usuário", validators = [DataRequired()])
    msg = StringField("Mensagem", validators = [DataRequired()])

class EditForm(FlaskForm):
    postID = StringField("ID do post", validators=[DataRequired()])
    newMsg = StringField("Nova mensagem do Post", validators=[DataRequired()])