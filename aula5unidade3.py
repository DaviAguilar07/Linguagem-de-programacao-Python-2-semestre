import sqlite3 
conn = sqlite3.connect('funcionarios.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS funcionario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cargo TEXT,
    salario REAL    
    )
""")


novo_funcionario = [('1', 'João', 'Maquinista', 4500), ('2', 'Maria', 'Cabeleleira', 5000),
                     ('3', 'Luiz', 'Designer', 2000), ('4', 'Eduarda', 'Apresentadora', 10000),
                       ('5', 'Paulo', 'Politico', 50000)]
cursor.executemany("INSERT INTO funcionario VALUES (?, ?, ?, ?)", novo_funcionario)

conn.commit()

cursor.execute("SELECT * FROM funcionario")
serviço = cursor.fetchall()

print("Funcionários cadastrados")
for funcionario in serviço:
    print(serviço)

atualizaçao = ("UPDATE funcionario SET nome = ? WHERE id = ?", 'João Silva', 4)
cursor.execute(atualizaçao)
conn.commit()

deletando = ("DELETE FROM funcionario WHERE id = ?")
cursor.execute(deletando, 2)
