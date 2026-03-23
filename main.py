from services.cliente_service import(
    cadastrar_cliente,
    listar_clientes,
    buscar_cliente,
    remover_cliente,
    editar_cliente
)

def menu():
    print("\n" + "=" * 40)
    print(" SISTEMA DE CLIENTES")
    print("=" * 40)
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente")
    print("4 - Editar cliente")
    print("5 - Remover cliente")
    print("6 - Sair")   

def main():
    while True:
        menu()

        try:
            op = int(input("Escolha: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if op == 1:
            cadastrar_cliente()
        elif op == 2:
            listar_clientes()
        elif op == 3:
            buscar_cliente()
        elif op == 4:
            editar_cliente()
        elif op == 5:
            remover_cliente()
        elif op == 6:
            print("Encerrando sistema.")
            break
        else: print("Opção inválida.")


if __name__ == "__main__":
    main()
        