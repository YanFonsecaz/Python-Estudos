# Criar duas novas funcoes: cadastrar usuario(cliente) e cadastrar conta bancária e vincular com o cliente

# funcao de saque deve receber os argumentas apenas por nome (keyword only) argumentos:saldo,valor,extrato,limete,numero_saques,limite_saques e retorna saldo e extrato
usuarios = []
contas_correntes = []
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

# funcao de deposito deve receber os arumentos apenas por posicao (positional only). argumentos: saldo valor, extrato e retorna saldo e extrato
# Comentário de função: Realiza depósito para o usuário identificado pelo CPF. Atualiza saldo e extrato.
def depositar(valor,/):
    cpf = input("Informe o CPF do usuário: ").strip().replace(".","").replace("-","")
    identificar_se_usuario_existe = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    if identificar_se_usuario_existe:
        identificar_se_usuario_existe["saldo"] += valor
        identificar_se_usuario_existe["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Usuário não encontrado.")

# Sacar
# Comentário de função: Realiza saque para o usuário identificado pelo CPF. Verifica limite de saques e saldo.
def sacar(*,valor):
    cpf = input("Informe o CPF do usuário: ").strip().replace(".","").replace("-","")
    identificar_se_usuario_existe = next((usuario for usuario in usuarios if usuario["cpf"] == cpf),None)
    if identificar_se_usuario_existe:
        if identificar_se_usuario_existe["numero_saques"] >= LIMITE_SAQUES:
            print("Limite de saques excedido.")
            return
        if valor > identificar_se_usuario_existe["saldo"]:
            print("Saldo insuficiente.")
            return
        
        identificar_se_usuario_existe["saldo"] -= valor
        identificar_se_usuario_existe["extrato"] += f"Saque: R$ {valor:.2f}\n"
        identificar_se_usuario_existe["numero_saques"] += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Usuário não encontrado.")

#funcao extrato deve receber os argumentos por posicao e nome (positional only e keyword only). argumentos posicionais:saldo, argumentos nomeados: extrato
# Comentário de função: Imprime saldo e extrato do usuário identificado pelo CPF.
def extrato_bancario():
    cpf = input("Informe o CPF do usuário: ").strip().replace(".","").replace("-","")
    identificar_se_usuario_existe = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    if identificar_se_usuario_existe:
        print(f"Saldo atual: R$ {identificar_se_usuario_existe['saldo']:.2f}")
        if identificar_se_usuario_existe["extrato"]:
            print(identificar_se_usuario_existe["extrato"])
        else:
            print("Não foram realizadas movimentações.")
    else:
        print("Usuário não encontrado.")

# Criar usuario (cliente) O programa deve armazenar os usuarios em uma lista, um usuario é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. deve ser armazenado apenas os numeros do cpf. nao pode ser armazenado 2 usuarios com o mesmo cpf.

# Comentário de função: Cadastra um novo usuário (cliente) validando CPF único e inicializando saldo/extrato/numero_saques.
def cadastrar_usuario():
        nome = input("Informe o nome do usuário: ").strip()
        data_nascimento = input("Informe a data de nascimento do usuário: ").strip()
        cpf = input("Informe o CPF do usuário: ").strip().replace(".","").replace("-","")
        endereco = input("Informe o endereço do usuário: logradouro, nro - bairro - cidade/sigla estado ").strip()
            
        cpf_existente = any(usuario["cpf"] == cpf for usuario in usuarios)
        if cpf_existente:
            print("CPF já cadastrado.")
            return
        else:
            usuarios.append({
                "nome": nome,
                "data_nascimento": data_nascimento,
                "cpf": cpf,
                "endereco": endereco,
                "saldo": 0,
                "extrato": "",
                "numero_saques": 0
            })
            print("Usuário cadastrado com sucesso.")
            print("\n Lista de usuários cadastrados:")
        for usuario in usuarios:
            print(usuario)

# criar conta corrente o programa deve armazenar contas em uma lista, uma conta é composta por: agencia, numero da conta e usuario. o numero da conta é sequencial, iniciando em 1. o numero da agencia é fixo: "0001". O usuario pode ter mais de uma conta, mas uma conta pertence a apenas um usuario.

# Comentário de função: Cadastra uma conta corrente vinculada a um usuário existente via CPF.
def cadastrar_conta_corrente(usuarios):
    cpf = input("Informe o CPF do usuário: ").strip().replace(".","").replace("-","")

    identificar_se_usuario_existe = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    if identificar_se_usuario_existe:
        agencia = "0001"
        numero_conta = len(contas_correntes) + 1
        contas_correntes.append({
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": identificar_se_usuario_existe
    })
        print("Conta corrente cadastrada com sucesso.")
    else:
        print("Usuário não encontrado.")

while True:
    menu = """ 
        [c] Cadastrar usuário
        [u] Cadastrar conta corrente
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    """
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor <= 0:
            print("Valor de depósito deve ser maior que zero.")
            continue
        depositar(valor)
        continue
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        if valor <= 0:
            print("Valor de saque deve ser maior que zero.")
            continue
        sacar(valor=valor)
        continue
    elif opcao == "e":
        extrato_bancario()
    elif opcao == "c":
        cadastrar_usuario()
        continue
    elif opcao == "u":
        cadastrar_conta_corrente(usuarios)
        continue
    elif opcao == "q":
        print("Saindo do programa.")
        break

# Dica
#para vincular um usuario a uma conta, filtre a lista de usuarios buscando o numero do CPF informado para cada usuario da lista