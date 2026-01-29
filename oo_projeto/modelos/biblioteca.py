class Biblioteca:
  bibliotecas = []
  
  def __init__(self, name):
    self.name = name
    self._ativo = False
    Biblioteca.bibliotecas.append(self)
    
  def __str__(self):
    return self.name
  
  def listar_bibliotecas():
    for biblioteca in Biblioteca.bibliotecas:
      print(f"{biblioteca}")
      
  def alterna_estado(self):
    self._ativo = not self._ativo
  
  @property
  def ativo(self):
   return "ativado" if self._ativo else "desativado"
   
  

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

Biblioteca.listar_bibliotecas()
print(vars(biblioteca_cidade))