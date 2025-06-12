import random

def gerar_numero_aleatorio():
    """
        Gerar números aleatorios imprimindo 10 números entre 1 a 100 
    """
    print("Bem vindo ao gerador de numeros aleatorios")
    
    numero_aleatorios = []
    
    #Gera os numeros aleatorios 
    for _ in range(10):
        numero = random.randint(1,100) # gera um aleatorio de 1 a 100
        numero_aleatorios.append(numero)
        
    print("\nNumeros aleatorios sao: ")
    
    for i , numero in enumerate(numero_aleatorios, start= 1):
     print(f'Numero {i} : {numero}')
    
    
if __name__ =='__main__':
    gerar_numero_aleatorio()