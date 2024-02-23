import mysql.connector
import re

config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'voicebot',
    'port': '3306'
}

def filtrar_entrada(entrada):
    padrao = re.compile(r'[^a-zA-Z0-9À-ú]')

    if isinstance(entrada, str):
        return padrao.sub('', entrada)
    elif isinstance(entrada, dict):
        entrada_filtrada = {}
        for chave, valor in entrada.items():
            if isinstance(valor, str):
                valor_filtrado = padrao.sub('', valor)
                entrada_filtrada[chave] = valor_filtrado
            else:
                entrada_filtrada[chave] = valor
        return entrada_filtrada
    else:
        raise TypeError("Tipo de entrada recusado")


def inserir_cargo(cargo):
    try:
        with mysql.connector.connect(**config) as conn, conn.cursor() as cursor:
            cursor.execute("INSERT INTO cargo (cargo) SELECT %s WHERE NOT EXISTS (SELECT 1 FROM cargo WHERE cargo = %s)", (cargo, cargo))
            conn.commit()
            print(f"Cargo '{cargo}' inserido com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao inserir cargo: {e}")

def inserir_usuario(data):
    try:
        with mysql.connector.connect(**config) as conn, conn.cursor() as cursor:
            cursor.execute("SELECT id_cargo FROM cargo WHERE cargo = %s", (data['cargo'],))
            cargo_id = cursor.fetchone()

            if cargo_id:
                cargo_id = cargo_id[0]
                sql = "INSERT INTO documento (cpf, primeiro_nome, ultimo_nome, data_nascimento, cargo) VALUES (%s, %s, %s, %s, %s)"
                val = (data['cpf'], data['primeiro_nome'], data['ultimo_nome'], data['data_nascimento'], cargo_id)
                cursor.execute(sql, val)
                conn.commit()
                return True, 'Usuário adicionado com sucesso!'
            else:
                return False, f"Cargo '{data['cargo']}' não encontrado na tabela 'cargo'."
    except (mysql.connector.Error, KeyError) as e:
        return False, f'Erro: {e}'

def test_inserir_usuario():
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

    success, message = inserir_usuario(data_teste_2)
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

test_inserir_usuario_interativo()
