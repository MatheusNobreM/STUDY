class Biblioteca:
    bibliotecas = []

    def __init__(self, name):
        self.name = name
        self._ativo = False
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.name

    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'Nome da biblioteca:'.ljust(20)} | {'Status:'}")
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca} | {biblioteca.ativo}")

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "ativado" if self._ativo else "desativado"
