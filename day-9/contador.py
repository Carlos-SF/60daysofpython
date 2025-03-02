# Um contador que para quando atinger um valor definido pelo usuario

def contador_personalizado():
    try: 
        limite =  int(input('Digite o valor maximo do contado: '))
        # função range crua uma lista de numeros a partir do 0 
        # ate o valor definidopelo usuario
        limite = limite + 1
        for i in range(limite): 
            print(i)
            if i == limite:
                print('Contador atindgiu o limite')
                break
    except ValueError:
        print('Entrada invalida. Por favor insira um número')

contador_personalizado()