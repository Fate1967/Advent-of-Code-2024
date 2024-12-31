import re
import pandas as df

LINHAS = 140
COLUNAS = 140

class Lente:
    def __init__(self, data):
        self.data = data
        # Coordenada atual
        self.coordenada = (0,0)
        self.cursor = (0,0)
        # Um segmento 4x4 dos dados
        self.foco = self.getDados(self.coordenada)

    def down(self):
        l, c = self.coordenada
        if (l < LINHAS-3):
            self.coordenada = (l+1, c)
        else:
            print("Fim")
            l = LINHAS-4

    def up(self):
        l, c = self.coordenada
        if (l != 0):
            self.coordenada = (l-1, c)
        else:
            print("Início")
            l = 0  

    def right(self):
        l, c = self.coordenada
        if (c < COLUNAS-3):
            self.coordenada = (l, c+1)
        else:
            print ("Margem D")
            c = COLUNAS-4

    def left(self):
        l, c = self.coordenada
        if (c > 0):
            self.coordenada = (l, c-1)
        else:
            print ("Margem E")
            c = 0

    # Retorna os dados em foco como uma matriz 4x4
    # Obtém o conjunto de dados da coordenada
    def getDados(self, coordenada) -> list:    
        linha = coordenada[0]
        coluna = coordenada[1]

        cache = []
        cache.append(self.data.at[linha,0][coluna])
        cache.append(self.data.at[linha, 0][coluna+1])
        cache.append(self.data.at[linha, 0][coluna+2])
        cache.append(self.data.at[linha, 0][coluna+3])

        cache.append(self.data.at[linha+1,0][coluna])
        cache.append(self.data.at[linha+1, 0][coluna+1])
        cache.append(self.data.at[linha+1, 0][coluna+2])
        cache.append(self.data.at[linha+1, 0][coluna+3])

        cache.append(self.data.at[linha+2,0][coluna])
        cache.append(self.data.at[linha+2, 0][coluna+1])
        cache.append(self.data.at[linha+2, 0][coluna+2])
        cache.append(self.data.at[linha+2, 0][coluna+3])

        cache.append(self.data.at[linha+3,0][coluna])
        cache.append(self.data.at[linha+3, 0][coluna+1])
        cache.append(self.data.at[linha+3, 0][coluna+2])
        cache.append(self.data.at[linha+3, 0][coluna+3])

        self.matriz = cache
        self.coordenada = (linha, coluna)
        return self.matriz

    def _cache(self) -> list:
        txt = ""
        cache = []
        for e in self.foco:
            txt += e
        cache.append(txt)
        return cache

    def getXMAS(self) -> int:
        temp = re.findall('XMAS', self._cache[0])
        return len(temp)

    def getSAMX(self) -> int:
        temp = re.findall('SAMX', self._cache[0])
        return len(temp)
    
    def transformaColunasEmLinhas(self) -> list:
        cache = []
        for c in range(4):
            palavra = self.foco[c][0] + self.foco[c][1]+self.foco[c][2]+self.foco[c][3]
            cache.append(palavra)
            cache.insert(temp[c][])

        return cache


# --------------------------------------------------------------------------------------    
#                                  *** MAIN ***
# --------------------------------------------------------------------------------------
def main():

    PATH = "input"
    flag = True
    dados = df.read_fwf(PATH, header=None)

    # Variáveis de resultado
    xmas_totalLinhas = 0
    xmas_totalColunas = 0
    xmas_totalTransversoED = 0
    xmas_totalTransversoDE = 0
    # --
    samx_totalLinhas = 0
    samx_totalColunas = 0
    samx_totalTransversoED = 0
    samx_totalTransversoDE = 0

    # Objetivo: escanear uma área de 4x4 a procura da palavra chave
    # em todas as direções, anotar, discriminar e totalizar resultados
    # progredir para o próximo campo e assim até o final do conjunto de dados
    # Linha : 136 Coluna: 136 é o último alvo possível na amostra 140x140
    # Scanner
    lente = Lente(dados)
    
    while(flag):

        # Interface
        print()
        print ("\n                  Scanner de Dados - v 0.3")
        print ("            Interaja com: '>', '<', 'A', 'V' ou 'Q'")
        print ("            ---------------------------------------")
        print ("                XMAS                    SAMX")
        print (" Linha: \t", xmas_totalLinhas, "\t\t\t", samx_totalLinhas)
        print (" Coluna: \t", xmas_totalColunas, "\t\t\t", samx_totalColunas)
        print (" Transv.ED: \t", xmas_totalTransversoED, "\t\t\t", samx_totalTransversoED)
        print (" Transv.DE: \t", xmas_totalTransversoDE, "\t\t\t", samx_totalTransversoDE)

        print()
        print (" Coordenada atual: ", lente.coordenada)
        print (lente.getDados(lente.coordenada))
        cmd = input(" > ")
        # Quit
        if (cmd == 'Q'): quit()
        # DOWN
        if (cmd == 'V'): lente.down()
        # UP
        if (cmd == 'A'): lente.up()
        # FORWARD
        if (cmd == '>'): lente.right()
        # REWIND
        if (cmd == '<'): lente.left()
        # XMAS
        if (cmd == 'X'): lente.getXMAS()
        # Transforma
        if (cmd == 'T'): lente.transformaColunasEmLinhas()
    # Loop  

if __name__ == '__main__':
    main()