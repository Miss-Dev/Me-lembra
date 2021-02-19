from flask import Flask, render_template, request, redirect, flash
import os
from formulario import form_cadastro, form_login, form_lembrete, csrf
import utils
from sqlalchemy.sql import select


# auth = HTTPBasicAuth()
app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf.init_app(app)



@app.route("/", methods=['GET', 'POST'])
def home():
    login = form_login()
    
    if login.validate_on_submit():
        i = utils.consultar(request.form['email'])
        if i==True:
            user = utils.verificar(request.form['email'])
            if user.senha == request.form['senha']:
                print('-------------------------')
                print(request.form['email'])            
                print('-------------------------')        
                return redirect('/success/'+request.form['email']+'/') 
        else:
            flash("Login ou senha estão incorretos!")   
    return render_template('index.html', form=login)


@app.route("/success/<string:email>/", methods=["GET", "POST"])
def principal(email):    
    if request.method == 'GET':
        if utils.consultar(email)==False: 
           return redirect("/") 
    email_user = str(email)  
    lembretes = utils.listar_lembretes()  
    return render_template('principal.html', variavel=email_user, lembretes = lembretes)

@app.route("/lembrete/<string:email>/", methods=["GET", "POST"])
def lembrete(email):
    if request.method == 'GET':
        if utils.consultar(email)==False: 
           return redirect("/")
    lembrete = form_lembrete()    
    if lembrete.validate_on_submit():        
        print('-------------------------')
        print(request.form['titulo'])            
        print('-------------------------') 
        utils.insert_lembrete(request.form['titulo'], request.form['descricao'], email)       
    else:
        flash("Está faltando alguma informação")   
    return render_template('lembrete.html', form= lembrete)

@app.route("/cadastro", methods=['GET','POST'])
def cadastro():
    form = form_cadastro()
    
    if form.validate_on_submit() and request.form['senha']==request.form['senha_confirm']:
        print('-------------------------')
        print(request.form['email'])            
        print('-------------------------')        
        if utils.consultar(request.form['email'])==False:
            utils.cadastrar(request.form['email'], request.form['senha']) 
            return redirect('/success/'+request.form['email']+'/')  
        else: 
            flash("Usuário já tem cadastro!")           
       
    return render_template('cadastro.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)