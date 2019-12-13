valores= {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X':10, 'V':5, 'I':1}

def romano_a_arabigo(letra):
    resultado = 0
    ultimoCaracter = ''
    numRepes = 0
    for i in range(len(letra)):
        if letra[i] == ultimoCaracter:
            numRepes +=1
        else:
            numRepes = 1

        if ultimoCaracter == 'V' and valores[ultimoCaracter] < valores[letra[i]]:
            return 0

        if ultimoCaracter == 'L' and valores[ultimoCaracter] < valores[letra[i]]:
            return 0
        
        if ultimoCaracter == 'D' and valores[ultimoCaracter] < valores[letra[i]]:
            return 0
        

        if numRepes > 3:
            return 0

        if i < len(letra)-1:
            if valores[letra[i]] >= valores[letra[i+1]]:
                resultado += valores[letra[i]]
            else:
                resultado -= valores[letra[i]]
        else:
            resultado += valores[letra[i]]
        
        ultimoCaracter = letra[i]

    return resultado

