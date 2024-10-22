#Função para converter data
def converter_data(dia, mes, ano):
    if mes < 10:
        if dia < 10:
            data = f'{ano}-0{mes}-0{dia}'
        else:
            data = f'{ano}-0{mes}-{dia}'
    else:
        if dia < 10:
            data = f'{ano}-{mes}-0{dia}'
        else:
            data = f'{ano}-{mes}-{dia}'    
    return data