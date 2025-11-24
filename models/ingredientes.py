def adiciona_ingrediente(data, nome, quantidade, unidade="un"):
    nome = nome.lower()
    ing = data["ingredientes"]

    if nome in ing:
        ing[nome]["quantidade"] += quantidade
    else:
        ing[nome] = {"quantidade": quantidade, "unidade": unidade}


def deduz_ingrediente(data, nome, quantidade):
    nome = nome.lower()
    ing = data["ingredientes"]

    if nome not in ing:
        raise ValueError(f"Ingrediente '{nome}' não existe.")

    if ing[nome]["quantidade"] < quantidade:
        raise ValueError(f"Quantidade insuficiente de '{nome}'.")

    ing[nome]["quantidade"] -= quantidade


def checa_quant_ingrediente(data, nome):
    nome = nome.lower()
    ing = data["ingredientes"]

    return ing[nome]["quantidade"] if nome in ing else None


def lista_ingredientes(data):
    return data["ingredientes"].copy()


def checa_ingrediente(data, nome):
    return nome.lower() in data["ingredientes"]
