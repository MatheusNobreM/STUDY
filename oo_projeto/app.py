from modelos.biblioteca import Biblioteca

biblioteca_shopping = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")


def main():
    Biblioteca.listar_bibliotecas()


if __name__ == "__main__":
    main()
