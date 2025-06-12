import random
def jogo_adivinhacao():
    """
        Um jogo onde o usuario tenta adivinhar um numero aleatorio
    """
    print("Bem vindo ao nosso jogo de adivinhacao")
    
    #Gera um numero secreto de 0 a 10 
    numero_secreto = random.randint(0,10)    
    
    tentativas = 0 
    
    while True: 
        try:
            palpite = int(input("Digite o seu palpite"))
            tentativas  += 1
            if palpite < numero_secreto:
                print("Muito abaixo do numero secreto ")
            elif palpite > numero_secreto: 
                print("Muito alto em relação ao numero secreto  ")
            else :
                print(f" Parabéns você acerto : O numero {numero_secreto}, suas tentativas fora  {tentativas}")
                break  
        except ValueError:
            print("DIGITE UM NUMERO VALIDO DE 0 A 10 !!!!")       
            
if __name__ == "__main__":
      jogo_adivinhacao()   
       
    