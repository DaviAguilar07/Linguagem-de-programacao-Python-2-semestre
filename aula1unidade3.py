import sqlite3

conn = sqlite3.connect('login.db')
cursor = conn.cursor()

# Criando tabela
create_table = ("""
CREATE TABLE IF NOT EXISTS CADASTRO(
    id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT
);
""")
cursor.execute(create_table)

# Inserindo pessoas
adicionando_pessoas = [
    ('João', 'joao@gmail.com', '5555-5555'),
    ('José', 'jose@gmail.com', '1111-1111'),
    ('Maria', 'maria@gmail.com', '8888-8888'),
    ('Luna', 'luna@gmail.com', '7777-7777'),
]

inserindo_pessoas = "INSERT INTO CADASTRO (nome, email, telefone) VALUES (?, ?, ?)"
cursor.executemany(inserindo_pessoas, adicionando_pessoas) #Executar várias linhas na tabela.

conn.commit()
conn.close()


#Exibindo a tabela original
conn = sqlite3.connect('login.db')
cursor = conn.cursor()

lendo_lista = "SELECT * FROM CADASTRO"
cursor.execute(lendo_lista)

clientes = cursor.fetchall()
for cliente in clientes:# Imprimindo a lista em diferentes linhas
    print(cliente)

conn.close()


# Update na tabela

conn = sqlite3.connect('login.db')
cursor = conn.cursor()


atualizaçao_tabela = "UPDATE CADASTRO SET nome = ? WHERE id = ?"
cursor.execute(atualizaçao_tabela, ("Maria Luiza", 4))

conn.commit()
conn.close()

# Delete na tabela

conn = sqlite3.connect('login.db')
cursor = conn.cursor()

deletar_usuario = "DELETE FROM CADASTRO WHERE id = 1"

cursor.execute(deletar_usuario)

conn.commit()
conn.close()


# Impressão após o update e o delete

conn = sqlite3.connect('login.db')
cursor = conn.cursor()


lendo_lista = "SELECT * FROM CADASTRO"
cursor.execute(lendo_lista)

clientes = cursor.fetchall()
for cliente in clientes:
    print(cliente)

conn.close()
