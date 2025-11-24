import models.cardapio as cardapio
import models.estoque as estoque
import models.ingredientes as ingredientes


def main():
    data = {"ingredientes": {}, "cardapio": {}}

    # exemplos de uso
    ingredientes.adiciona_ingrediente(data, "tomate", 10)
    cardapio.cria_item_cardapio(data, "salada", 12.0, {"tomate": 2})
    estoque.gera_venda(data, "salada")


if __name__ == "__main__":
    main()
