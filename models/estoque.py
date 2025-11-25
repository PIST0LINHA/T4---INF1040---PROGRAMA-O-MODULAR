<<<<<<< HEAD
import models.ingredientes as ingredientes

=======
import ingredientes
>>>>>>> refs/remotes/origin/main

def deduz_item(data, nome, quantidade):
    nome = nome.lower()
    card = data["cardapio"]

    if nome not in card:
        raise ValueError("Item não pertence ao cardapio")

    ing_item = card[nome]["ingredientes"]

    for item_ingredientes in ing_item:
        ingredientes.deduz_ingrediente(data, item_ingredientes, quantidade)

    return True


def adiciona_item(data, nome, quantidade, unidade="un"):
    ingredientes.adiciona_ingrediente(data, nome, quantidade, unidade)


def checa_quant_item(data, nome):
    return ingredientes.checa_quant_ingrediente(data, nome)


def checa_ingredientes(data):
    return data["ingredientes"]


def altera_item(data, nome, nova_quant):
    nome = nome.lower()
    ing = data["ingredientes"]

    if nome not in ing:
        raise ValueError("Ingrediente não encontrado")
    else:
        ing[nome]["ingredientes"] = nova_quant
