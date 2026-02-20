import sqlite3

conexao = sqlite3.connect("titulo.db")
cursor = conexao.cursor()

dados = cursor.execute("SELECT * FROM filmes")

print(dados.fetchall())
