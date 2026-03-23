from models.cliente import Cliente
from utils.storage import carregar_dados, salvar_dados
from utils.validadores import validar_cpf, validar_email
from utils.logger import log_info, log_error, log_warning

def cadastrar_cliente():
    try:
        print("\n=======    CADASTRAR CLIENTE   =======")

        nome = input("Nome: ").strip()
        cpf = input("CPF: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("E-mail: ").strip()

        if not nome or not cpf:
            print("Nome e CPF são obrigatórios.")
            return
        
        if not validar_cpf(cpf):
            print("CPF inválido.")
            return
        
        if not validar_email(email):
            print("E-mail inválido.")
            return

        clientes = carregar_dados()

        for c in clientes:
            if c["cpf"] == cpf:
                log_warning(f"Tentativa de cadastro duplicado | CPF={cpf}")
                print("Cliente já cadastrado com esse CPF.")
                return
        
        novo_cliente = Cliente(nome, cpf, telefone, email)
        clientes.append(novo_cliente.to_dict())

        salvar_dados(clientes)
        log_info(f"Cliente cadastrado: {cpf}")

        print("Cliente cadastrado com sucesso.")

    except Exception as e:
        log_error(f"Erro ao cadastrar cliente | ERRO={e}")
        print("Erro interno.")

def listar_clientes():
    print("\n======= LISTA DE CLIENTES =======")

    clientes = carregar_dados()

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    
    for c in clientes:
        print(f"{c['nome']} | CPF: {c['cpf']} | Tel: {c['telefone']} | E-mail: {c['email']}")

def buscar_cliente():
    cpf = input("Digite o CPF: ").strip()

    clientes = carregar_dados()

    for c in clientes:
        if c["cpf"] == cpf:
            print(f"\nNome {c['nome']}")
            print(f"CPF: {c['cpf']}")
            print(f"Telefone: {c['telefone']}")
            print(f"E-mail: {c['email']}")
        return
    
    print("Cliente não encontrado.")

def editar_cliente():
    cpf = input("CPF do cliente a editar: ").strip()
    clientes = carregar_dados()

    for c in clientes:
        if c["cpf"] == cpf:
            print("Cliente encontrado. Deixe vazio para não alterar.")

            novo_nome = input(f"Nome ({c['nome']}): ") or c["nome"]
            novo_tel = input(f"Telefone ({c['telefone']}): ") or c["telefone"]
            novo_email = input(f"Email ({c['email']}): ") or c["email"]

            if not validar_email(novo_email):
                print("Email inválido.")
                return

            c["nome"] = novo_nome
            c["telefone"] = novo_tel
            c["email"] = novo_email
            salvar_dados(clientes)

            log_info(f"Cliente editado: {cpf}")
            print("Atualizado.")
            return

    print("Cliente não encontrado.")


def remover_cliente():
    cpf = input("CPF do cliente a remover: ").strip()

    clientes = carregar_dados()

    novos = [c for c in clientes if c["cpf"] != cpf]

    if len(clientes) == len(novos):
        print("Cliente não encontrado")
        return
    
    salvar_dados(novos)
    log_info(f"Cliente removido: {cpf}")
    print("Cliente removido com sucesso.")

    