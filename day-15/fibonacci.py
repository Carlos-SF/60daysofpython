fibonacci = [0,1] # a sequenciade fibonacci sempre começa 0 e 1 

for i in range(8):
    proximo_numero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_numero)

print(fibonacci)
