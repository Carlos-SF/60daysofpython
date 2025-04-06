def anagrama(palavra1,palavra2):
     """
     Verificar  se duas palavras são um anagrama ou nãp
      :param palavra1: Primeira palavra 
      :param palavra2: Segunda palavra
      :çretun: True se as palavras forem um anagrama
     """
     #Removendo espaços e convertendo para letras minusculas
     palavra1 = palavra1.replace(" "," ").lower()
     palavra2 = palavra2.replace(" "," ").lower()
     
     if sorted(palavra1) == sorted(palavra2):
        return f'Essas palavras sao anagramas'
     return  f'Essas palavras nao sao aagrams'
 
print(anagrama('amor','roma'))