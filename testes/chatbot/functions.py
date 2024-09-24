import requests
import time
import pandas as pd

def execute_chatbot_tests(url: str, headers: dict, texto: str, num_tests: int = 8) -> pd.DataFrame:
    """
    Executa testes de interação com o chatbot e retorna um DataFrame com os resultados.

    :param url: URL da API do chatbot.
    :param headers: Cabeçalhos da requisição, incluindo token e username.
    :param texto: Texto a ser enviado ao chatbot.
    :param num_tests: Número de vezes que o teste deve ser executado.
    :return: DataFrame com os tempos de resposta e status das requisições.
    """
    response_times = []

    for i in range(num_tests):
        try:
            # Captura o tempo antes da requisição
            start_time = time.time()

            # Faz a requisição POST para o chatbot
            response = requests.post(url, data={'texto': texto}, headers=headers)

            # Captura o tempo após a requisição
            end_time = time.time()

            # Calcula o tempo total da requisição
            response_time = end_time - start_time

            response_json = response.json()
            resposta_voicebot = response_json.get('text', None)

            # Armazena o tempo de resposta e status da resposta na lista
            response_times.append({
                'Execução': i + 1,
                'Tempo de resposta (s)': response_time,
                'Status Code': response.status_code,
                'Resposta': resposta_voicebot
            })

            # Exibe o status de progresso
            print(f"Teste {i + 1}/{num_tests} concluído. Tempo de resposta: {response_time:.4f} segundos")
            print(resposta_voicebot)

        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição {i + 1}: {e}")
            # Adiciona erro à lista para manter consistência
            response_times.append({
                'Execução': i + 1,
                'Tempo de resposta (s)': None,
                'Status Code': 'Erro'
            })

    # Criando um DataFrame com os resultados
    df = pd.DataFrame(response_times)
    return df


def login_and_get_token(username: str, password: str) -> str:
    """
    Faz o login e retorna o access_token.

    :param username: O CPF do usuário para login.
    :param password: A senha do usuário para login.
    :return: O access_token se o login for bem-sucedido; caso contrário, uma mensagem de erro.
    """
    # URL de login
    url_login = "https://murilopreto.pythonanywhere.com/api/login"

    # Dados de login
    data = {
        'username': username,
        'password': password
    }

    # Cabeçalhos da requisição
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Faz a requisição POST para o login
    response = requests.post(url_login, data=data, headers=headers)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # A resposta é um JSON contendo o token
        response_json = response.json()
        
        # Acessa o token
        access_token = response_json.get('access_token', None)
        
        if access_token:
            return access_token
        else:
            return "Token não encontrado na resposta."
    else:
        return f"Falha no login. Status Code: {response.status_code}. Mensagem de erro: {response.text}"

# Exemplo de uso
if __name__ == "__main__":
    username = '123.123.123-00'  # Exemplo de CPF
    password = 'admin'  # Substitua pela senha correta
    token = login_and_get_token(username, password)
    print(f"Token de Acesso: {token}")
