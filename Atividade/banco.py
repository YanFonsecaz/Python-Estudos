# ================= TASKS ================= #
usuarios = []
contas_correntes = []
LIMITE_SAQUE = 500
numero_saque = 0

# 1. Criar função cadastrar_usuario()
# Comentário: Solicitar nome, data de nascimento, CPF e endereço. 
# Validar CPF único. Inicializar saldo=0, extrato="" e numero_saques=0. 
# Armazenar na lista 'usuarios'.

def cadastrar_usuario():
    print("================ Cadastrar Usuarios ======================")
    nome = input("informe seu nome: ").lower().strip()
    cpf = input("Informe seu CPF: ").replace(".","").replace("-",".")
    validando_CPF = next((usuario for usuario in usuarios if usuario["cpf"] == cpf),None)

    if validando_CPF:
        print("Usuario ja esta cadastrado!!")
        return

    data_nascimento = input("informe a data de nascimento: ")
    endereco = input("Informe seu endereço: ")

    novo_usuario = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
        "saldo": 0,
        "extrato": "",
        "numero_saques":0,
    }

    usuarios.append(novo_usuario)
    print(usuarios)

# 2. Criar função cadastrar_conta_corrente()
# Comentário: Solicitar CPF do usuário para vinculação.
# Verificar se usuário existe na lista 'usuarios'.
# Criar conta com agência fixa "0001" e número sequencial.
# Vincular a conta ao usuário e armazenar em 'contas_correntes'.

def cadastrar_conta_corrente():
    cpf = input("Informe seu CPF: ").strip().replace(".","").replace("-","")
    validacaoCPF = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    if not validacaoCPF:
        print("Usuario não cadastrado")
    else:
        id_contas = len(contas_correntes) + 1
        novo_conta_corrente = {
            "agencia": "0001",
            "id": id_contas,
            "cpf": cpf,
        }
        contas_correntes.append(novo_conta_corrente)
        print("Conta Corrente Cadastrada com Sucesso!!")


# 3. Modificar função depositar()
# Comentário: Receber argumentos apenas por posição (positional only).
# Atualizar saldo e extrato do usuário identificado pelo CPF.

def depositar(valor,/):

    if valor <= 0:
        print("Valor de deposito deve ser maior que zero")
        return

    cpf = input("Informe seu CPF").strip().replace(".","").replace("-","")
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

    if usuario:
        usuario["saldo"] += valor
        usuario["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print(f"Deposito de {valor:.2f} Realizado!!")
    else:
        print("Conta não existe")

# 4. Modificar função sacar()
# Comentário: Receber argumentos apenas por nome (keyword only).
# Verificar saldo suficiente e limite de saques.
# Atualizar saldo, extrato e numero_saques do usuário.

def saque(*, saque, limite = LIMITE_SAQUE):
    if saque <= 0:
        print("O valor do saque deve ser maior que zero")
        return
    if saque > limite:
        print(f"O valor de saque ultrapassa o limite:{limite}")
        return
    
    cpf = input("Informe seu CPF").strip().replace(".","").replace("-","")
    validacaoCPF = next((usuario for usuario in usuarios if usuario["cpf"] == cpf),None)

    if not validacaoCPF:
        print("Usuário não encontrado.")
        return
    
    if validacaoCPF["numero_saques"] >= 3:
        print("Seu limite diario de saque foi atingindo.")
        return
    
    if validacaoCPF["saldo"] < saque:
        print(f"Saldo insuficiente {validacaoCPF['saldo']:.2f}")
        return
    

    validacaoCPF["saldo"] -= saque
    validacaoCPF["extrato"] += f"Foi realizado o saque de {saque}"
    validacaoCPF["numero_saques"] += 1
    print(f"Saque de {saque}, realizado com sucesso!!")
    print(validacaoCPF['saldo'])

# 5. Modificar função extrato_bancario()
# Comentário: Receber argumentos mistos (positional-only e keyword-only).
# Imprimir saldo e extrato do usuário identificado pelo CPF.
def extrato_bancario():
    cpf = input("Informe o seu CPF: ").strip().replace("-","").replace(".","")
    validacaoCPF = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

    if validacaoCPF:
        print("======Saldo Atual======== ")
        print(validacaoCPF["saldo"])
        print()
        print("================Extrato================")
        print(validacaoCPF["extrato"])
    

# 6. Atualizar menu principal
# Comentário: Incluir opções para cadastrar usuário e conta.
# Chamar funções correspondentes corretamente.

while True:
    opcao = input("""
        [c] Cadastrar usuário
        [u] Cadastrar conta corrente
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    """).strip().lower()

    if opcao == "c":
        print("Bem vindo a seção de cadastro!!")
        cadastrar_usuario()
    elif opcao == "u":
        print("Crie uma conta-corrente!!")
        cadastrar_conta_corrente()
    elif opcao == "d":
        print("Realize um deposito")
        valor = float(input("informe o valor do deposito: "))
        depositar(valor)
    elif opcao == "s":
        print("Realize um Saque!!")
        saques = float(input("Digite o valor do saque:"))
        saque(saque=saques)
    elif opcao == "e":
        print("Extrato Bancario!!")
        extrato_bancario()
    elif opcao == "q":
        break
    else:
        print("Valor digitado incorreto!")