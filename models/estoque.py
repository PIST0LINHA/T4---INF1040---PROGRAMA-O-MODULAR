import ingredientes


def gera_venda(data, item):
    item = item.lower()
    card = data["cardapio"]

    if item not in card:
        raise ValueError("Item não existe no cardápio.")

    receita = card[item]["ingredientes"]

    for ing, qtd in receita.items():
        quant = ingredientes.checa_quant_ingrediente(data, ing)
        if quant is None:
            raise ValueError(f"Ingrediente '{ing}' não existe.")
        if quant < qtd:
            raise ValueError(f"Quantidade insuficiente de '{ing}'.")

    for ing, qtd in receita.items():
        ingredientes.deduz_ingrediente(data, ing, qtd)


def deduz_item(data, nome, quantidade):
    ingredientes.deduz_ingrediente(data, nome, quantidade)


def adiciona_item(data, nome, quantidade, unidade="un"):
    ingredientes.adiciona_ingrediente(data, nome, quantidade, unidade)


def checa_quant_item(data, nome):
    return ingredientes.checa_quant_ingrediente(data, nome)


def altera_item(data, nome, nova_quant):
    nome = nome.lower()
    ing = data["ingredientes"]

    if nome not in ing:
        raise ValueError("Ingrediente não existe.")

    ing[nome]["quantidade"] = nova_quant
