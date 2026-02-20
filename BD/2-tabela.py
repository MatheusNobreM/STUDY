import sqlite3

conexao = sqlite3.connect("titulo.db")

cursor = conexao.cursor()

cursor.execute(
    """
    CREATE TABLE filmes(
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      nome TEXT NOT NULL,
      ano INTEGER NOT NULL,
      nota REAL NOT NULL
    )
  """
)

conexao.close()
print("Tabela foi criada")
