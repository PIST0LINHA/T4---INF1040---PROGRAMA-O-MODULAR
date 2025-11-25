import models.estoque as estoque


def gera_venda(data, nome_prato, quantidade):
    """
    Controller: gerenciar a logica de venda
    1. checa se existe prato
    2. checa os ingredientes
    3. deduz os ingredientes (via model)
    """

    ingredientes_necessarios = estoque.checa_ingredientes(data)

    if not ingredientes_necessarios:
        return False, f"prato '{nome_prato}' não encontrado no cardápio"

    for ingrediente, quant_por_prato in ingredientes_necessarios:
        quant_total_necessaria = quant_por_prato * quantidade
        quant_disponivel = estoque.checa_quant_item(data, ingrediente)

        if quant_disponivel < quant_total_necessaria:
            return False, (
                f"venda falhou: estoque insuficiente de '{ingrediente}'."
                f"necessario: '{quant_total_necessaria}', disponivel: '{quant_disponivel}'."
            )

    for ingrediente, quant_por_prato in ingredientes_necessarios.items():
        quant_total_necessaria = quant_por_prato * quantidade
        sucesso = estoque.deduz_item(data, ingrediente, quant_total_necessaria)

        if not sucesso:
            return False, f"Erro inesperado ao deduzir ingrediente: {ingrediente}"
        return True, f"Venda de {quantidade}x '{nome_prato}' registrada com sucesso"
