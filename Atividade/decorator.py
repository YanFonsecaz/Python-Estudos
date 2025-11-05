import functools
def log_execucao(saudacao):
    @functools.wraps(saudacao)
    def envelope():
        print("Executando função...")
        saudacao()
        print("Funcao finalizado!")
    return envelope

@log_execucao
def saudacao():
    print("Ola, mundo!")

print(saudacao.__name__)

def log_soma(somar):
    @functools.wraps(somar)
    def envolepe(*args,**kwargs):
        print("recebendo valores")
        resultado = somar(*args,**kwargs)
        print("Calculo Finalizado")
        return resultado
    return envolepe

@log_soma
def somar(a,b):
    print("A soma de {a} + {b}")
    return a + b

print(somar(2,2))

import time

def tempo_execucao(tarefa_pesada):
    def envolepe(*args,**kwargs):
        inicio = time.time()
        resultado = tarefa_pesada(*args,**kwargs)
        fim = time.time()
        duracao = fim - inicio
        print(f"Tempo de execução: {duracao:.2f}")
        return resultado
    return envolepe

@tempo_execucao
def tarefa_pesada():
    for _ in range(10_000_000):
        pass

print(tarefa_pesada())