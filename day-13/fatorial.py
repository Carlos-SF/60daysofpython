# O que é um fatorial : é um calculo em matemarica onde multiplicamos os valores apartir dos numeros passados 
#  ex 5! 5 x 4 5 x 3 5 x 2 5 x 1 = 120 
def fatorial(n):
    """Calcula o fatorial de um numero usando recursão.
    :param n: Numero inteiro não negativo.
    :return: Fatorial de n .
    """
    if n < 0:
        raise ValueError('O numero deve ser positivo') # levanta a exeção
    # então essa condicional retorna 1 se caso o numero da funcao for 0 ou 1
    if n == 0 or n == 1:
        return 1
    #  tratando com recursividade 
    return n * fatorial(n - 1)

# print(fatorial(5))
# print(fatorial(1))


try:
    print(f'Fatorial igual a {fatorial(12)}')
except ValueError as e :
    print(e) 