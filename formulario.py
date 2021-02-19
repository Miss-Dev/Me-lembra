from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import PasswordInput

csrf = CSRFProtect()

class form_cadastro(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])    
    senha = StringField('Senha', validators=[DataRequired("Campo obrigatório!")], widget=PasswordInput(hide_value=False))
    senha_confirm = StringField('Confirmar senha', validators=[DataRequired("Confirme sua senha please!")], widget=PasswordInput(hide_value=False))

class form_login(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired("Campo obrigatório")])
    senha = StringField('Senha', validators=[DataRequired("Campo obrigatório!")], widget=PasswordInput(hide_value=False))

class form_lembrete(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired("Campo Obrigatório")])
    descricao = TextAreaField('Descrição', validators=[DataRequired("Campo Obrigatório")])