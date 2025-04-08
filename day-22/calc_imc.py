def calcular_imc():
    """Função que calcula o imc
    """
    
    print('Bem vindo a calculadora de IMC')

    try: 
        peso = float(input('Digite o seu peso em KG: '))
        
        altura = float(input('Digite sua altura em metros: '))
        
        if peso < 0 or altura < 0: 
            print('O peso e altura deve ser maior que 0')
            
        imc = round(peso / (altura **2),2)
        
        if imc < 18.5: 
            print('Você esta abaixo do peso')
        elif 18.5 <=  imc <= 24.9: 
            print('Você está no peso normal')
        elif 25 <=  imc <= 29.9:
            print('Você esta de sobrepeso ')
        else :
            print('Você esta com obsidade ')
            
    except ValueError: 
        print('a entrada esta invavalida')

# Significa que estamos rodando esse codigo internamete
# apenas  rodar se eu rodar o meu script calcular_imc
if __name__ == '__main__':
    calcular_imc()