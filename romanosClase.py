valores= {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X':10, 'V':5, 'I':1}
posiciones= {'I':1, 'V':2, 'X': 3, 'L':4, 'C':5, 'D': 6, 'M':7}



def contarParentesis
def romano_a_arabigo(letra):
    resultado = 0
    ultimoCaracter = ''
    numRepes = 1

    for letra in letra:

        if letra in valores:
            resultado += valores[letra]
            if ultimoCaracter == '':
                pass
            elif valores[ultimoCaracter] > valores[letra]:
                numRepes = 1
            elif valores[ultimoCaracter] == valores[letra]:
                numRepes += 1

                if numRepes > 3:
                    return 0
                
                if letra in ['V','L','D']:
                    return 0
            else:
                if numRepes > 1:
                    return 0
                elif ultimoCaracter in ['V','L','D']:
                    return 0
                elif posiciones[letra] - posiciones[ultimoCaracter] > 2:
                    return 0
                else:
                    resultado -= valores[ultimoCaracter]*2
                    numRepes = 1
        else:
            return 0
        
        ultimoCaracter = letra

    return resultado

