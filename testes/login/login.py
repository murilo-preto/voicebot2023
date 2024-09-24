import requests
import time
import pandas as pd

# URL da API de login
url = "https://murilopreto.pythonanywhere.com/api/login"

# Dados de login (substitua pelos dados reais de teste)
data = {
    'username': '123.123.123-00',  # Exemplo de CPF
    'password': 'admin'    # Substitua pela senha de teste
}

# Cabeçalhos da requisição
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Número de testes
n = 500

# Lista para armazenar os tempos de resposta
response_times = []

# Executando o teste n vezes
for i in range(n):
    try:
        # Captura o tempo antes da requisição
        start_time = time.time()

        # Faz a requisição POST
        response = requests.post(url, data=data, headers=headers)

        # Captura o tempo após a requisição
        end_time = time.time()

        # Calcula o tempo total da requisição
        response_time = end_time - start_time

        # Armazena o tempo de resposta na lista
        response_times.append({
            'Execução': i + 1,
            'Tempo de resposta (s)': response_time,
            'Status Code': response.status_code
        })

        # Exibe o status de progresso
        print(f"Teste {i + 1}/{n} concluído. Tempo de resposta: {response_time:.4f} segundos")

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

# Exibindo a tabela de tempos de resposta
print("\nTabela de tempos de resposta:")
print(df)

# Se quiser salvar os resultados em um arquivo CSV, descomente a linha abaixo:
df.to_csv('tempos_resposta_login.csv', index=False)