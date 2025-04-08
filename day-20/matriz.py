def trampor_matriz(matriz):
    """
    Gerar uma matriz tramposta de 3x3 
    Substituir colunas horizintais por verticais 
    
    Exemplo :  
    
    {1,2,3}
    {1,2,3}
    {1,2,3}
    
     {1,1,1}
     {2,2,2}
     {3,3,3}
     
     Arg Matriz  que vão listar de 3 numeros na horizontal e vertical 
     Return Matriz tramsposta
     Raises: ValueError : Se a Matriz não ter 3x3 
    """
    # verificador se a matriz é 3x3 
    if len(matriz) != 3 or not all(len(linha) == 3 for linha in matriz):
         raise ValueError('A matriz não possui o tamanho 3 x3 ')
     #Gerar matriz transposta 
    transposta  = [[matriz[j] [i] for j in range(3)] for i in range(3)]
    return transposta 

matriz = [
    [1,2,3],
    [1,2,3],
    [1,2,3]
]

for linha in trampor_matriz(matriz):
    print(linha)
