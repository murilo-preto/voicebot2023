import pandas as pd
import numpy as np

# Passo 1: Carregar o arquivo CSV
df = pd.read_csv('tempos_resposta_login.csv')

# Passo 2: Selecionar a coluna com os dados numéricos (substitua 'coluna_desejada' pelo nome real)
dados_numericos = df['Tempo']

# Passo 3: Calcular a mediana
mediana = np.median(dados_numericos)
media = np.average(dados_numericos)

# Exibir o resultado
print(f'A mediana é: {mediana}')
print(f'A média é: {media}')
