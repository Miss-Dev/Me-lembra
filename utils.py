from models import Usuarios, Lembretes

def cadastrar(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consultar(login):  
    usuario = Usuarios.query.filter_by(login=login).first()
    if usuario is None:
        print("não encontrei")
        return False
        # return False
    return True
    print("encontrei")   

def verificar(login):
    if consultar(login)==True:
        return Usuarios.query.filter_by(login=login).first()

def listar_usuarios():
    nomes = Usuarios.query.all()
    print(nomes)

def exclui_pessoa(login):
    pessoa = Usuarios.query.filter_by(login=login).first()
    pessoa.delete()

def insert_lembrete(titulo, texto, usuario):
    lembrete = Lembretes(titulo = titulo, texto = texto, usuario_id = usuario)
    lembrete.save()

def listar_lembretes(email):
    lemb = Lembretes.query.all()
    lemb_result = []
    for i in lemb:
        if i.usuario_id == email:
            lemb_result.append(i)
    return lemb_result



if __name__ == '__main__':
    # cadastrar("samyhurtadoramos@gmail.com", "1234")
    # consultar("samyhurtadoramos@gmail.com")
    listar_lembretes("samyhurtadoramos@gmail.com")
    