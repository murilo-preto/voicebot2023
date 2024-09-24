import requests
import pandas as pd
from functions import login_and_get_token, execute_chatbot_tests
import os

# URL da API do chatbot
url = "https://murilopreto.pythonanywhere.com/api/chatbot"

# Texto a ser enviado ao chatbot
texto_enviar_voicebot = 'sim'

# Número de vezes que os testes devem ser executados
num_executions = 75  # Substitua pelo número desejado de execuções
resultados_totais = pd.DataFrame()  # DataFrame para armazenar todos os resultados
csv_file_path = 'chatbot/tempos_resposta_chatbot_consolidados.csv'  # Caminho do arquivo CSV

# Cria o arquivo CSV se não existir
if not os.path.exists(csv_file_path):
    resultados_totais.to_csv(csv_file_path, index=False)

try:
    # Executa os testes múltiplas vezes
    for execucao in range(num_executions):
        access_token = login_and_get_token(
            username='123.123.123-00', password='admin')

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'token': access_token,
            'username': 'admin'  # Nome de usuário
        }

        print(f"\nExecutando teste {execucao + 1}/{num_executions}...")
        df_resultados = execute_chatbot_tests(url, headers, texto_enviar_voicebot)

        # Adiciona os resultados do teste atual ao DataFrame total
        resultados_totais = pd.concat(
            [resultados_totais, df_resultados], ignore_index=True)

        # Salva os resultados parciais em um arquivo CSV após cada execução
        df_resultados.to_csv(csv_file_path, mode='a', index=False, header=False)

except (Exception, KeyboardInterrupt) as e:
    if isinstance(e, KeyboardInterrupt):
        print("Execução interrompida pelo usuário.")
    else:
        print(f"Ocorreu um erro: {e}")
    
    # Salvando os resultados parciais em um arquivo CSV em caso de erro ou interrupção
    resultados_totais.to_csv(
        'chatbot/tempos_resposta_chatbot_parciais.csv', index=False)
    print("Resultados parciais salvos em 'chatbot/tempos_resposta_chatbot_parciais.csv'.")
    # Termina a execução
    exit()

# Exibindo a tabela consolidada de tempos de resposta
print("\nTabela consolidada de tempos de resposta:")
print(resultados_totais)

# Salvando todos os resultados em um arquivo CSV (opcional, já estão salvos após cada execução)
# resultados_totais.to_csv(
#     csv_file_path, index=False)
