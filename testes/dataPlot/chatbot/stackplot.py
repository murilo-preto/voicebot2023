import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importar dados do arquivo CSV
df = pd.read_csv('chatbot\chatbot_dados.csv')

# Definir cores utilizando uma paleta mais ampla do Matplotlib
unique_interactions = df['Interacao'].unique()
colors = plt.get_cmap('tab20').colors  # Usando a paleta 'tab20' para mais cores

# Configurações do gráfico
plt.figure(figsize=(14, 8))  # Tamanho ajustado para 14x8 para melhor visualização

# Preparar dados para o stackplot
time_bins = np.linspace(df['Tempo_execucao'].min(), df['Tempo_execucao'].max(), 100)
densities = []

# Calcular densidades para cada interação
for interaction in unique_interactions:
    execution_times = df[df['Interacao'] == interaction]['Tempo_execucao']
    density, _ = np.histogram(execution_times, bins=time_bins, density=True)
    densities.append(density)

# Convertendo densidades para um array numpy
densities = np.array(densities)

# Criar o stackplot com ajustes visuais
plt.stackplot(time_bins[:-1], densities, labels=unique_interactions, colors=colors, alpha=0.6, baseline='zero')

# Ajustes dos eixos
plt.xlim(df['Tempo_execucao'].min(), 2.3)  # Remover limite rígido de 2.3
# plt.ylim(0, np.max(densities) * 1.1)  # Ajuste do eixo Y para mostrar 10% acima do valor máximo

# Configurações do gráfico
plt.title('Distribuição do Tempo de Execução por Interação (Stackplot)', fontsize=22)
plt.xlabel('Tempo de Execução (s)', fontsize=16)
plt.ylabel('Densidade', fontsize=16)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(title='Interações', fontsize=12)
plt.tight_layout()

# Mostrar o gráfico
plt.show()
