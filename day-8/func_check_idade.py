def pode_digrigir(idade):
    if idade >= 18:
        return True
    else:
        return False
print(pode_digrigir(18))

try:
    input_user =int(input('Digite a sua idade : '))
    print(pode_digrigir(input_user))
except ValueError: 
    print('Entrada invalida. Por favor, digite um numero inteiro')