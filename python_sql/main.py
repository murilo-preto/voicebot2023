import mysql.connector

# Configurações de conexão
config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'voicebot',
    'port': '3306'  # Porta padrão do MySQL
}

# Estabelecer conexão
try:
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print('Conexão estabelecida com sucesso!')
        cursor = connection.cursor()

       # Executar o comando SHOW TABLES
        cursor.execute("SHOW TABLES;")
        
        # Recuperar resultados
        tables = cursor.fetchall()
        
        # Imprimir as tabelas
        print("Tabelas no banco de dados:")
        for table in tables:
            print(table[0])

except mysql.connector.Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")

finally:
    # Fechar a conexão
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão encerrada.")
