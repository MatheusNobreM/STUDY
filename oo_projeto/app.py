from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

# biblioteca_shopping.receber_avaliacao("Fulano", 9)
# biblioteca_shopping.receber_avaliacao("2", 10)

livro1 = Livro("1984", "George Orwell", 30.0, "0800-987")
revista1 = Revista("National Gergraphic", "Jorge", 20.0, "Quinta")


biblioteca_cidade.adicionar_item(livro1)
biblioteca_cidade.adicionar_item(revista1)

livro1.aplicar_desconto()


def main():
    # Biblioteca.listar_bibliotecas()
    biblioteca_cidade.exibir_itens()


if __name__ == "__main__":
    main()
