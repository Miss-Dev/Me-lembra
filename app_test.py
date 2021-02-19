from flask import Flask, request, render_template, redirect
from flask_restful import Resource, Api
import os
from formulario import form_cadastro, form_login, csrf
from db.models import Usuarios, Lembretes
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)



@auth.verify_password
def verificacao(login, senha):
    if not(login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()

