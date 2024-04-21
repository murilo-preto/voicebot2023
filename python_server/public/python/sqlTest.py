import mysql.connector
from sqlFunctions import inserir_usuario, inserir_login

config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'voicebot',
    'port': '3306'
}

def test_inserir_usuario(selector):
    data_teste_1 = {
        'cpf': '12345678900',
        'primeiro_nome': 'João',
        'ultimo_nome': 'Silva',
        'data_nascimento': '1990-01-01',
        'cargo': 'paciente'
    }

    data_teste_2= {
        'cpf': '34567890155',
        'primeiro_nome': 'Álvaro',
        'ultimo_nome': 'Torres',
        'data_nascimento': '1970-09-25',
        'cargo': 'medico'
    }

    usuarios = [data_teste_1, data_teste_2]

    success, message = inserir_usuario(usuarios[selector])
    print(success, message)


def test_inserir_usuario_interativo():
    print("Teste de inserção de usuários - Modo Interativo\n")

    while True:
        print("Por favor, insira os dados do novo usuário:")
        cpf = input("CPF: ")
        primeiro_nome = input("Primeiro Nome: ")
        ultimo_nome = input("Último Nome: ")
        data_nascimento = input("Data de Nascimento (AAAA-MM-DD): ")
        cargo = input("Cargo: ")

        novo_usuario = {
            'cpf': cpf,
            'primeiro_nome': primeiro_nome,
            'ultimo_nome': ultimo_nome,
            'data_nascimento': data_nascimento,
            'cargo': cargo
        }

        success, message = inserir_usuario(novo_usuario)

        if success:
            print(f"\nUsuário adicionado com sucesso: {message}\n")
        else:
            print(f"\nFalha ao adicionar usuário: {message}\n")

        opcao = input("Deseja inserir outro usuário? (s/n): ")
        if opcao.lower() != 's':
            print("Encerrando o teste de inserção de usuários.")
            break

# test_inserir_usuario[0]
inserir_login(cpf='12345678900', senha='12345')