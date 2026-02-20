import sqlite3

conexao = sqlite3.connect("titulo.db")
cursor = conexao.cursor()

id = 2, 3
cursor.execute(
    """
  DELETE FROM filmes
  WHERE ID in (?,?)
  """,
    id,
)

conexao.commit()
conexao.close()

print("Dados Deletados")
