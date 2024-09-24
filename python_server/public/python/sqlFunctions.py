import mysql.connector
import re
import bcrypt

config = {
    'user': 'murilopreto',
    'password': 'mysql31415@',
    'host': 'murilopreto.mysql.pythonanywhere-services.com',
    'database': 'murilopreto$voicebot'
}

def gen_hash_password(salt, senha):
    senha = senha.encode('utf-8')

    hash_senha = bcrypt.hashpw(senha, salt)
    return hash_senha


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


def inserir_login_nativo(cpf, senha):
    try:
        with mysql.connector.connect(**config) as conn, conn.cursor() as cursor:
            cursor.callproc('inserir_login', (cpf, senha))

            for result in cursor.stored_results():
                message = result.fetchone()[0]
                print(message)
    except mysql.connector.Error as e:
        print(f'Erro ao inserir login: {e}')

def inserir_login_server_hash(cpf, senha):
    try:
        with mysql.connector.connect(**config) as conn, conn.cursor() as cursor:
            cursor.execute("SELECT id FROM documento WHERE cpf = %s", (cpf,))
            user_id = cursor.fetchone()

            if user_id:
                user_id = user_id[0]
                sql = "INSERT INTO login (id_documento, salt, hash_senha) VALUES (%s, %s, %s)"

                salt = bcrypt.gensalt()
                hash_senha = gen_hash_password(salt, senha)

                print(f"Senha {senha} ; Salt {salt} ; Hash {hash_senha}")

                val = (user_id, salt, hash_senha)
                cursor.execute(sql, val)
                conn.commit()
                return True, 'Usuário adicionado com sucesso!'
            else:
                return False, f"Erro: Não foi possível encontrar o user_id."
    except (mysql.connector.Error, KeyError) as e:
        return False, f'Erro: {e}'


def validar_login_nativo(cpf, senha):
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

def validar_login_server_hash(cpf, senha):
    try:
        with mysql.connector.connect(**config) as conn, conn.cursor() as cursor:
            cursor.execute("SELECT id FROM documento WHERE cpf = %s", (cpf,))
            id_documento = cursor.fetchone()

            if id_documento:
                function_call = "SELECT salt FROM login WHERE id_documento = %s"
                cursor.execute(function_call, id_documento)
                salt = cursor.fetchone()[0]

                function_call = "SELECT hash_senha FROM login WHERE id_documento = %s"
                cursor.execute(function_call, id_documento)
                hash_senha_db = cursor.fetchone()[0]

                hash_senha = gen_hash_password(salt=salt, senha=senha)

                if (hash_senha==hash_senha_db):
                    return True, "Senha validada com sucesso"

            return False, "Erro ao validar senha"

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