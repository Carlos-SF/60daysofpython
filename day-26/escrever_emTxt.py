def escrever_arquyivo(nome_arquivo, conteudo):
    
    """  
        Escrever : O nome do arquivo a ser criado ou sobreecrito
        
        Arg: 
        nome_arquivo(): O nome do arquivo a ser ccriado ou sobreescrito 
        contendo  (str) : O texto que vai ser escrito no arquivo 
    
    """
    
    with open(nome_arquivo,'w') as arquivo: # w = write 
        arquivo.write(conteudo)
    print(f'O conteudo ofi salvo no arquivo {nome_arquivo}. ')
    
    
def ler_arquivo(nome_arquivo):
    """
        Ler o conteudo do arquivo .txt
        
        Arg: 
            nome_arquivo(str) O nome do arquivo a ser lido 
    """
    try :
        with open(nome_arquivo, 'r') as arquivo: # r = read 
           conteudo=  arquivo.read()
        print(f'Counteudo do arquivo: {conteudo}')
    except FileExistsError:
        print("O arquivo nao fo iencontrado")
        
def main(nome_arquivo, conteudo):
    """
        Funcao principal que demonstra escrita e leitura do nosso arquivo

    Args:
         nome_arquivo(): O nome do arquivo a ser ccriado ou sobreescrito 
        contendo  (str) : O texto que vai ser escrito no arquivo 
    """
    
    print("Bem vindo ao nosso arquivo")
    #Escrevendo no arquivo 
    escrever_arquyivo(nome_arquivo,conteudo)
    #leitura do arquivo 
    print("Fazendo a leitura do arquivo")
    
    ler_arquivo(nome_arquivo)
    
    
    
if __name__ == '__main__':
    arquivo = 'exemplo.txt'
    texto = 'Modificar o texto'
    main(arquivo,texto )
 