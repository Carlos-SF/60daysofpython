def busca_linear(lista, numero_procurado):
# doc string  é documentação que colocamos no nosso codigo para documentar o que cada função faz 
    """
     Procurar um numero dentro de uma lista buscando linear
     : Param lista : çosta de numeros
     : Param numero_procurado: o numero que procurar
    """
    for i, numero in enumerate(lista): # funcao nativa do python enumerate 
    #enumerate passa por cada item dentro de uma lista enquanto contabiliza 
         if numero == numero_procurado:
             return i
    return - 1   

lista = [10,2,4,6,7,8,11]
numero_procurado = 11


buscando_o_numero = busca_linear(lista,numero_procurado)
print(buscando_o_numero)

if buscando_o_numero != -1:
    print(f'O numero se entrado no indice : {buscando_o_numero}')
else: 
    print('Numero não encontrado é ')
# for i, numero  in enumerate(['ackercode',1,2,3,4,5,6,7,8,9]):
#     print(f'Indoce:  {i} e objeto {numero}')