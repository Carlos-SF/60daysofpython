# random fornece funções para gerar numeros aleatorios
import random
# string fornece um conjunto de caracteres prontos como letras maisculas, numeros e simbolos
import string

def gerador_de_senha(tamanho):
    comprimento = tamanho 
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    
    while len(senha) < comprimento:
        senha += random.choice(caracteres)
    
    print(f'Sua senha ficou assim : {senha}') #print senha
    
gerador_de_senha(9)