import sqlite3

conn = sqlite3.connect('MinhaLoja.db')
cursor = conn.cursor()

#Criando a tabela (CREATE)
create_table = """
CREATE TABLE IF NOT EXISTS PRODUTOS(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preço REAL NOT NULL,
    estoque INTEGER)"""

cursor.execute(create_table)
conn.commit()
conn.close()



#Inserindo dados na tabela
conn = sqlite3.connect('MinhaLoja.db')
cursor = conn.cursor()

novo_produto = ('Camiseta', 19.99, 50)
inserir_produto = "INSERT INTO PRODUTOS (nome, preço, estoque) VALUES (?, ?, ?)"

cursor.execute(inserir_produto, novo_produto)
conn.commit()
conn.close()

print('Produto inserido.')


#Lendo a tabela (READ)
conn = sqlite3.connect('MinhaLoja.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM Produtos")
produtos = cursor.fetchall()

for produto in produtos:
    print(produto)

conn.close()



#Modificando dados na tabela (UPDATE)
conn = sqlite3.connect('MinhaLoja.db')
cursor = conn.cursor()


novo_preço = 25.85
produto_id = 1

cursor.execute(

     "UPDATE PRODUTOS SET preço = ? WHERE id = ?",
    (novo_preço, produto_id)

)

conn.commit()
conn.close()
print('Produto atualizado.')


#Utilizando o DELETE
conn = sqlite3.connect('MinhaLoja.db')
cursor = conn.cursor()

produto_id = 2

cursor.execute("DELETE FROM Produtos WHERE id = ?", (produto_id,))

conn.commit()
conn.close()

print('Produto excluído.')
