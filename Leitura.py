import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="endpoint",  
    user="login", 
    password="senha",
    database="banco"
)

query = "SELECT * FROM tabela_escolhida"  

df = pd.read_sql(query, conn)

conn.close()
