import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="endpoint",  
    user="login", 
    password="senha",
    database="banco"
)

cursor = conn.cursor()

df = pd.read_csv(r"caminho")
nome_tabela = "tabela_seleiconada"

colunas = ", ".join([f"`{col}` VARCHAR(255)" for col in df.columns])
sql_create_table = f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({colunas});"
cursor.execute(sql_create_table)

for _, row in df.iterrows():
    valores = tuple(row)
    placeholders = ", ".join(["%s"] * len(row)) 
    sql_insert = f"INSERT INTO {nome_tabela} VALUES ({placeholders})"
    cursor.execute(sql_insert, valores)

conn.commit()

cursor.close()
conn.close()
