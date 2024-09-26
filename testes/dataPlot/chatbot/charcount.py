import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando o arquivo CSV
csv_path = 'chatbot_dados.csv'
df = pd.read_csv(csv_path)

# Adicionando a coluna 'caracteres', que contém a contagem de caracteres da coluna 'texto'
df['caracteres'] = df['texto'].apply(len)

# Definindo um estilo mais elegante para o gráfico
# sns.set(style="whitegrid")

# Criando o gráfico de regressão com um tamanho maior e cores aprimoradas
plt.figure(figsize=(14, 8))

# Plotando os pontos (scatter) e a linha de regressão
sns.regplot(x='Tempo_execucao', y='caracteres', data=df, 
            scatter_kws={'s': 5, 'color': 'blue', 'label': 'Pontos de Dados'}, 
            line_kws={'color': 'red', 'linewidth': 2, 'label': 'Curva de Regressão'})

# Adicionando título e rótulos personalizados
plt.title('Relação entre Tempo de Resposta e Número de Caracteres', fontsize=22)
plt.xlabel('Tempo de resposta (s)', fontsize=16)
plt.ylabel('Número de Caracteres', fontsize=16)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Adicionando a legenda ao gráfico
plt.legend(fontsize=12)

# Ajustando os ticks dos eixos para torná-los mais legíveis
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Exibindo o gráfico final
plt.show()
