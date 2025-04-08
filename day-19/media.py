def calcular_media_notas(notas):
    """
    Calculo media de notas a partir de uma lsita de notas
    Arg:
    notas(lista)
    
    Return: 
    float de media da notas 
    """
    media = sum(notas)// len(notas) #2
    
    #round arredondar a nossa media para duas casa decimais
    return round(media, 2)


print(calcular_media_notas([10,4,5,6,7,8]))