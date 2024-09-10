import mysql.connector

conn = mysql.connector.connect(
    host="endpoint",  
    user="login", 
    password="senha",
    database="banco"
)

cursor = conn.cursor()

alter_table_query = """
ALTER TABLE tabela_selecionada 
CHANGE coluna_atual coluna_nova Tipo;
"""

try:
    cursor.execute(alter_table_query)
    conn.commit()
    print("Colunas renomeadas com sucesso.")
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    cursor.close()
    conn.close()
