def cria_item_cardapio(data, nome, preco, ingredientes):
    nome = nome.lower()
    card = data["cardapio"]

    if nome in card:
        raise ValueError("Item já existe no cardápio.")

    card[nome] = {"preco": preco, "ingredientes": ingredientes}


def exclui_item_cardapio(data, nome):
    nome = nome.lower()
    card = data["cardapio"]

    if nome not in card:
        raise ValueError("Item não existe.")

    del card[nome]


def altera_item_cardapio(data, nome, preco=None, ingredientes=None):
    nome = nome.lower()
    card = data["cardapio"]

    if nome not in card:
        raise ValueError("Item não existe.")

    if preco is not None:
        card[nome]["preco"] = preco

    if ingredientes is not None:
        card[nome]["ingredientes"] = ingredientes
