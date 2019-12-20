class RomanNumber():
    __valores= {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X':10, 'V':5, 'I':1}
    __posiciones= {'I':1, 'V':2, 'X': 3, 'L':4, 'C':5, 'D': 6, 'M':7}

    __rangos = {
        0: {1: 'I', 5 : 'V', 'next': 'X'},
        1: {1: 'X', 5 : 'L', 'next': 'C'},
        2: {1: 'C', 5 : 'D', 'next': 'M'},
        3: {1: 'M', 'next': ''}
    }

    def __init__(self, value):
        self.value = value
        self.__romanValue = self.__arabigo_a_romano()
    

    def __invertir(self, cad):
        return cad[::-1]

    def __dividirgt1000(self):
        strnumArabigo = str(self.value)
        inv = self.__invertir(strnumArabigo)
        numP=0
        div = []
        
        for i in range(len(inv)-1,-1, -3):
            numP = int(i/3)
            if i>0 and len(inv) >= 3:
                div.append([numP,int(inv[i+2:i-1:-1])])
            else:
                div.append([numP,int(inv[i+2::-1])])
        
        for j in range(len(div)-1):
            grupoMayor = div[j]
            grupoMenor = div[j+1]
            unidadesMayor = grupoMayor[1] % 10

            if unidadesMayor < 4:
                grupoMenor[1] = grupoMenor[1] + unidadesMayor * 1000
                grupoMayor[1] = grupoMayor[1] - unidadesMayor
            
        return div

    def __arabigo_individual(self, numArabigo):
        convRomano = ''
        inv = self.__invertir(str(numArabigo))
        #Lo primordial de este bucle es que se recorreo al reves. Por ejemplo, num 3589. primero
        #lo invertimos 9853 y lo recorremos de atras para adelante, por lo que la iteracion del
        # for sera de 3 a -1, esto es importante porque el 3 del indice determina los miles.
        for i in range(len(inv)-1,-1,-1):
            if inv[i] <= '3':
                convRomano += self.__rangos[i][1]*int(inv[i])

            elif inv[i] == '4':
                convRomano += self.__rangos[i][1] + self.__rangos[i][5]

            elif inv[i] == '5':
                convRomano += self.__rangos[i][5]

            elif inv[i] >= '6' and inv[i]<= '8':
                convRomano += self.__rangos[i][5] + self.__rangos[i][1]*(int(inv[i])-5)

            elif inv[i] == '9':
                convRomano += self.__rangos[i][1] + self.__rangos[i]['next']
            
            else:
                return 0
        
        return convRomano

    def __arabigo_a_romano(self):
        g1000 = self.__dividirgt1000()
        romanoGlobal = ''
        for grupo in g1000:
            numero = grupo[1]
            rango = grupo[0]

            if numero > 0:
                romanoGlobal += '('*rango + self.__arabigo_individual(numero) + ')'*rango
            else:
                pass
        
        return romanoGlobal 

    def __str__(self):
        return self.__romanValue

    def __repr__(self):
        return self.__romanValue
