def tabuada():
    """
        Essa funcao recebe um numero e retrona a tabuada desse numero
    """
    
    try: 
         #solicitar o nuemro para o suario
        numero = int(input("Digiete o numero para gerar a tabuada : "))\
            
        print(f"\nTamanho de {numero} : ")
        
        #gera a tabuada de 1 a 10 
        
        for i in range(1,11):
            resultado = numero  *i 
            print(f"{numero} X {i} = {resultado}")
    except ValueError:
       print("Digite um valor valido")

if __name__ == "__main__":
    tabuada()