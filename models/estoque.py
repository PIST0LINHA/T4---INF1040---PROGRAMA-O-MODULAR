import ingredientes

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
