import mysql.connector

conn = mysql.connector.connect(
    host="endpoint",  
    user="login", 
    password="senha",
    database="banco"
)
cursor = conn.cursor()

insert_query = """
INSERT INTO tabela_selecionada (colunax, colunay) 
VALUES (%s, %s);
"""

# Valores a serem inseridos
valores = ("valorx", "valory")

try:
    cursor.execute(insert_query, valores)
    conn.commit()
    print("Dados inseridos.")
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    cursor.close()
    conn.close()
