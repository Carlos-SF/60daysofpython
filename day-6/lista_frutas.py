# # listade frutras
# frutas = ['banana','maça','melão','melancia']

# for fruta in frutas:
#     print(fruta)
    
# utilizando input para criar a lista de frutas

frutas = []
while True:
    fruta = input('Digite o nome das frutas: ')
    if fruta == 'sair':
        break
    frutas.append(fruta)
print(frutas)