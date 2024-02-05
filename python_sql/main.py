import mysql.connector

config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'voicebot',
    'port': '3306'  # Porta padrão do MySQL
}

def inserir_usuario(data):
    try:
        # Conexão com o banco de dados
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # Inserção de um novo usuário na tabela 'documento'
        sql = "INSERT INTO documento (cpf, primeiro_nome, ultimo_nome, data_nascimento, cargo) VALUES (%s, %s, %s, %s, %s)"
        val = (data['cpf'], data['primeiro_nome'], data['ultimo_nome'], data['data_nascimento'], data.get('cargo'))
        cursor.execute(sql, val)

        # Commit da transação
        conn.commit()

        # Fechar cursor e conexão
        cursor.close()
        conn.close()

        return True, 'Usuário adicionado com sucesso!'
    except mysql.connector.Error as e:
        error_message = f'Erro ao adicionar usuário: {str(e)}'
        return False, error_message
    except KeyError as e:
        error_message = f'Erro nos dados do usuário: {str(e)}'
        return False, error_message
    except Exception as e:
        error_message = f'Erro desconhecido: {str(e)}'
        return False, error_message

def test_inserir_usuario():
    # Caso de teste 1: Inserção bem-sucedida de um novo usuário
    data_teste_1 = {
        'cpf': '12345678900',
        'primeiro_nome': 'João',
        'ultimo_nome': 'Silva',
        'data_nascimento': '1990-01-01',
        'cargo': 'Analista'
    }
    success, message = inserir_usuario(data_teste_1)
    print(success, message)

test_inserir_usuario()
