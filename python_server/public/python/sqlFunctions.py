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
    

def inserir_login(cpf, senha):
    try:
        with mysql.connector.connect(**config) as conn, conn.cursor() as cursor:
            cursor.callproc('inserir_login', (cpf, senha))

            for result in cursor.stored_results():
                message = result.fetchone()[0]
                print(message)
    except mysql.connector.Error as e:
        print(f'Erro ao inserir login: {e}')

    
def validar_login(cpf, senha):
    try:
        with mysql.connector.connect(**config) as conn, conn.cursor() as cursor:
            cursor.execute("SELECT id FROM documento WHERE cpf = %s", (cpf,))
            id_documento = cursor.fetchone()

            if id_documento:
                function_call = "SELECT validar_login(%s, %s)"
                cursor.execute(function_call, (id_documento[0], senha))
                resultado = cursor.fetchone()[0]
                return resultado
            else:
                return False, f"Documento com CPF '{cpf}' não encontrado."
    except mysql.connector.Error as e:
        return False, f'Erro ao validar login: {e}'

def cpf_para_nome(cpf):
    try:
        with mysql.connector.connect(**config) as conn, conn.cursor() as cursor:
            cursor.execute("SELECT primeiro_nome FROM documento WHERE cpf = %s", (cpf,))
            nome = cursor.fetchone()

            if nome:
                return nome[0]
            else:
                return False, f"Documento com CPF '{cpf}' não encontrado."
    except mysql.connector.Error as e:
        return False, f'Erro ao validar login: {e}'