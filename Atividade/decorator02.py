import functools
def deletar_banco(user):
    @functools.wraps(deletar_banco)
    def envelope(*args,**kwargs):
        resultado = user()
        if resultado == "admin":
            print("Banco deletado!!")
            return
        else:
            print("Acesso negado!!!")
        return resultado
    return envelope



@deletar_banco
def user():
    acesso = input("Informe que tipo de acesso é o seu: ")
    return acesso

user()