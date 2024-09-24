from public.python.sqlFunctions import *

data_teste_1 = {
        'cpf': '12312312300',
        'primeiro_nome': 'admin',
        'ultimo_nome': 'admin',
        'data_nascimento': '2000-01-01',
        'cargo': 'admin'
    }

cargo = 'admin'

cpf = '12312312300'
senha = 'admin'

inserir_cargo(cargo)
inserir_usuario(data_teste_1)
inserir_login_server_hash(cpf, senha)

result, message = validar_login_server_hash(cpf, senha)
print(result, message)