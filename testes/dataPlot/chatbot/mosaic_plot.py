import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importar dados do arquivo CSV
df = pd.read_csv('chatbot/chatbot_dados.csv')

# Definir cores utilizando uma paleta mais ampla do Matplotlib
unique_interactions = df['Interacao'].unique()
colors = sns.color_palette('tab20', len(unique_interactions))  # Usando 'tab20' do Seaborn para cores

# Configurações do gráfico
fig, axs = plt.subplots(3, 3, figsize=(15, 10))  # Criando um mosaico 3x3
fig.suptitle('Distribuição do Tempo de Execução por Interação', fontsize=22)

# Iterar sobre as interações e criar gráficos com histplot
for i, interaction in enumerate(unique_interactions):
    # Definir o eixo correto no mosaico 3x3
    ax = axs[i // 3, i % 3]
    
    # Obter os tempos de execução da interação
    execution_times = df[df['Interacao'] == interaction]['Tempo_execucao']
    
    # Plotar histograma no subplot correspondente
    sns.histplot(execution_times, bins=30, kde=True, color=colors[i % len(colors)], ax=ax)
    
    # Adicionar título e labels
    ax.set_title(f'Interação {interaction}')
    ax.set_xlabel('Tempo de Execução (s)')
    ax.set_ylabel('Densidade')
    
    # Habilitar grade
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Plotar o total de todos os dados no último gráfico (posição 9)
# A posição é axs[2, 2] no mosaico 3x3
ax_total = axs[2, 2]
total_execution_times = df['Tempo_execucao']  # Todos os dados, desconsiderando a Interacao
sns.histplot(total_execution_times, bins=30, kde=True, color='gray', ax=ax_total)  # Cor 'gray' para diferenciar

# Adicionar título e labels ao gráfico total
ax_total.set_title('Total de Todos os Dados')
ax_total.set_xlabel('Tempo de Execução (s)')
ax_total.set_ylabel('Densidade')
ax_total.grid(True, which='both', linestyle='--', linewidth=0.5)

# Ajustar o espaçamento vertical entre os gráficos
plt.subplots_adjust(hspace=0.75)  # Aumentar o espaçamento vertical (hspace)

# Mostrar o gráfico
plt.show()
