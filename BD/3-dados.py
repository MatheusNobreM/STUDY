import sqlite3

conexao = sqlite3.connect("titulo.db")
cursor = conexao.cursor()

cursor.execute(
    """
  INSERT INTO filmes(nome, ano, nota)
  VALUES ('Lutas', 2022, 4)
  
  """
)

conexao.commit()
conexao.close()
print("Dados inseridos")
