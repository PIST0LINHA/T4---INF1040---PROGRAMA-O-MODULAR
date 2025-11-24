from models.estoque import (
    deduz_item,
    adiciona_item,
    checa_quant_item, 
    altera_item,
    checa_ingredientes,
)

def gera_venda(nome_prato, quantidade):
    """
    Controller: gerenciar a logica de venda
    1. checa se existe prato
    2. checa os ingredientes 
    3. deduz os ingredientes (via model)
    """

    ingredientes_necessarios = checa_ingredientes(nome_prato)

    if not ingredientes_necessarios:
        return False, f"prato '{nome_prato}' não encontrado no cardápio"
    
    for ingrediente, quant_por_prato in ingredientes_necessarios.items():
        quant_total_necessaria = quant_por_prato * quantidade
        quant_disponivel = checa_quant_item(ingrediente)

        if quant_disponivel < quant_total_necessaria:
            return False, (
                f"venda falhou: estoque insuficiente de '{ingrediente}'."
                f"necessario: '{quant_total_necessaria}', disponivel: '{quant_disponivel}'."
            )
        
    for ingrediente, quant_por_prato in ingredientes_necessarios.items():
        quant_total_necessaria = quant_por_prato * quantidade
        sucesso, msg = deduz_item(ingrediente, quant_total_necessaria)

        if not sucesso:
            return False, f"Erro inesperado ao deduzir ingrediente: {msg}"
        return True, f"Venda de {quantidade}x '{nome_prato}' registrada com sucesso"
    
    #delegacao do controller:

    deduz_item = deduz_item
    adiciona_item = adiciona_item
    checa_quant_item = checa_quant_item
    altera_item = altera_item