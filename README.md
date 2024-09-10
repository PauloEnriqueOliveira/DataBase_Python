# Leitura_DB

Esse repositório mostra alguns codigos de manipulação de banco de dados com Python usando o mysql.connector. Neste repositório você pode encontrar como ler e transformar tabelas em dataframes para o python, criar tabelas dentro do banco dentre outras informações. Qualquer dúvida, sinta-se à vontade para me chamar no [linkedin](https://www.linkedin.com/in/paulo-oliveira-a6650121a/).

## Descrição sobre cada file
- Criação_Tabelas - Este script tem como o intuito de gerar tabelas dentro do seu banco de dados e definir um csv para sua tabela;
- Leitura - A leitura serve para a leitura de qualquer tabela dentro do seu banco aonde além de estar lendo ela você pode estar trazendo ela para um dataframe para melhor manipulação de dados.
- mysql.connector [Biblioteca](https://www.mysql.com/products/connector/)
  
## Funções Base
#### - Conexão DB
~~~
conn = mysql.connector.connect(
    host="endpoint",  
    user="login", 
    password="senha",
    database="banco"
)
~~~
#### - Criação de Cursor
~~~
cursor = conn.cursor()
~~~
#### - Executar Query
~~~
cursor.execute("SELECT * FROM tabela_selecionada")
~~~
#### - Resultado da Query
~~~
result = cursor.fetchall()
~~~
#### - Inserção de informações na tabela
~~~
query = "INSERT INTO tabela (colunaX, colunaY) VALUES (%s, %s)"
valores = ("valorX", "valorY")
cursor.execute(query, valores)
conn.commit()
~~~
#### - Fechar conexão
~~~
cursor.close()
conn.close()
~~~
