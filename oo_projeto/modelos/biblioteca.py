from modelos.avaliacao import Avaliacao


class Biblioteca:
    bibliotecas = []

    def __init__(self, name):
        self.name = name
        self._ativo = False
        self._avaliacao = []
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.name

    @classmethod
    def listar_bibliotecas(cls):
        print(
            f"{'Nome da biblioteca:'.ljust(25)} | {'Nota média'.ljust(25)} | {'Status:'}"
        )
        for biblioteca in Biblioteca.bibliotecas:
            print(
                f"{biblioteca.name.ljust(25)} | {str(biblioteca.media_avaliacao).ljust(25)} | {biblioteca.ativo}"
            )

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "ativado" if self._ativo else "desativado"

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return "-"
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = round(soma / len(self._avaliacao), 1)

        return media
