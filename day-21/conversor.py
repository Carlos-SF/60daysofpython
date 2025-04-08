def  conversor(valor,taxa_cambio,tipo_conversao):
    """
    Essa funcao converter dolar em reais e visse versa 
    Args:
        valor: (float) Valor a ser convertido (monetario)
        taxa_cambio: A taxa de cambio atual
        tipo_conversao:dolar para real e ral para dolar 
        
    Return :
        float: O valor convertido, arredondado  para 2 casas decimais 
    
    Raises: 
        valueError: Se o tipode conversão for errado 
    """
    
    if tipo_conversao  == 'dolar_real':
        return round(valor * taxa_cambio, 2)
    elif tipo_conversao == 'real_dolar':
        return round(valor / taxa_cambio,2)
    else: 
        return ValueError('Tipode conversão invalida ')
    
print(conversor(12,6.91, 'real_dolar'))