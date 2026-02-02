from modelos.biblioteca import Biblioteca

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

biblioteca_shopping.receber_avaliacao("Fulano", 9)
biblioteca_shopping.receber_avaliacao("2", 10)


def main():
    Biblioteca.listar_bibliotecas()


if __name__ == "__main__":
    main()
