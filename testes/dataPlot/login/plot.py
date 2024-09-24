import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_pandas = pd.read_csv('tempos_resposta_login.csv')

# Melhorando a estética do gráfico de histograma

plt.figure(figsize=(12,8))

# Customizando o estilo do gráfico
sns.set(style="whitegrid")

# Histograma com mais bins e cores mais suaves
sns.histplot(df_pandas['Tempo'], bins=100, kde=True, color='blue', edgecolor='black', linewidth=1)

# Ajustando o título e os rótulos com fontes maiores e negrito
plt.title('Histograma dos tempos de execução para Login', fontsize=20, fontweight='bold')
plt.xlabel('Tempo (segundos)', fontsize=16, fontweight='bold')
plt.ylabel('Frequência', fontsize=16, fontweight='bold')

# Personalizando os limites do gráfico para melhor visualização
plt.xlim(df_pandas['Tempo'].min(), 2.5)
# plt.ylim(0, df_pandas['Tempo'].value_counts().max() * 1.1)

# Adicionando legendas, caso necessário, com a curva KDE
plt.legend(['Distribuição'], loc='upper right', fontsize=12)

# Grid com menos destaque para evitar poluição visual
plt.grid(True, alpha=0.3)

# Exibir o gráfico atualizado
plt.show()
