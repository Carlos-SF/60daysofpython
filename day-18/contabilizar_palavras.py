def contar_palavras(texto):
    """
        Contar palavras em uma string 
        :para texto String de entrada 
        :return Numero de palavras 
    
    """
    # Vai separar as palavras usando o espaço entre as palavras 
    palavras = texto.split()
    
    return len(palavras)

# texto = 'Oi tudo bem ? Como vai você ?'
# palavra = texto.split()
# print(palavra)
    