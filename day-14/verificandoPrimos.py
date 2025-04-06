numero  = int(input('Digite o numero para verificar se ele é primo: '))

# assumindo com true primeiramento uma variavel 
eh_primo = True 

if numero <= 1: 
    eh_primo =False

for i in range(2, int(numero ** 0.5) + 1): # testamso apenas até a raiz quadrada do numero 
    if numero %i == 0: # Verifica se o numero divisilver for primo 
        eh_primo = False
        break # saimos do loop 
    
if eh_primo: 
    print(f'{numero} eh  numero priomo')
else: 
    print(f'{numero} não é um numero primo')