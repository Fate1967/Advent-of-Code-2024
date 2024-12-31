import re
import pandas as pd
import pandas as df

# Entrada tem 140 por 140 caracteres


# Transforma matriz de caracteres em uma matriz de string
def assimila(dadoBruto: list) -> list:

    dadoAssimilado = []
    dado = ""
    for e in dadoBruto:
        dado += e

    dadoAssimilado.append(dado)
    return dadoAssimilado


# ***************************************************************************
#                                   MAIN
# ***************************************************************************
def main():

    file_path = "input"
    LINHAS = 140
    COLUNAS = 140
    OBJETO = 'XMAS'
    invOBJETO = OBJETO[::-1]
    # REGEX
    xmas_pat = rf'{OBJETO}'
    inv_xmas_pat = rf'{invOBJETO}'
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

    #           INÍCIO ------------------------------------------------------

    entrada = pd.read_fwf(file_path, header=None)   



    # Abordagem das LINHAS --------------------------------------------------
    linhas = re.findall(xmas_pat, entrada.to_string())
    xmas_totalLinhas = len(linhas)

    print (" Contagem de XMAS em linhas: ", xmas_totalLinhas)
    print ()

    linhas.clear()
    linhas = re.findall(inv_xmas_pat, entrada.to_string())
    samx_totalLinhas = len(linhas)
    print (" Contagem de SAMX em linhas: ", samx_totalLinhas)
    print ()




    # Abordagem das COLUNAS -------------------------------------------------
    temporaria = []
    cache = []

    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            # Note a inversão dos valores de coluna e linha
            temporaria.append(entrada.at[coluna,0][linha])
        # Loop
        coluna = 0

    # De caracteres > para uma string
    cache = assimila(temporaria)
    # matrizTransposta é mais versátil
    matrizTransposta = df.DataFrame(cache)
    
    colunas = re.findall(xmas_pat, matrizTransposta.to_string())
    xmas_totalColunas = len(colunas)
    print (" Contagem de XMAS em colunas: ", xmas_totalColunas)
    print ()

    colunas.clear()
    colunas = re.findall(inv_xmas_pat, matrizTransposta.to_string())
    samx_totalColunas = len(colunas)
    print (" Contagem de SAMX em colunas: ", samx_totalColunas)
    print ()



    # Abordagem da TRANSVERSAL ESQUERDA -------------------------------------
    temporaria.clear()
    for linha in range(LINHAS-3):
        # Armazena TRANSVERSA ED na lista 'temporaria'
        for caracter in range(COLUNAS - 3):   # Itera entre cada caracter (0 a 136)
            a1 = entrada.at[linha, 0][caracter]
            a2 = entrada.at[linha+1, 0][caracter+1]
            a3 = entrada.at[linha+2, 0][caracter+2]
            a4 = entrada.at[linha+3, 0][caracter+3]
            temporaria.append(a1+a2+a3+a4)
        # Loop
    # Loop
    cache.clear()
    TransversalEDmatrizTransposta = df.DataFrame(temporaria)

    # XMAS
    cache = re.findall(xmas_pat, TransversalEDmatrizTransposta.to_string())
    xmas_totalTransversoED = len(cache)
    print (" Contagem de XMAS em transversalED: ", xmas_totalTransversoED)
    print ()

    # SAMX
    cache.clear()
    cache = re.findall(inv_xmas_pat, TransversalEDmatrizTransposta.to_string())
    samx_totalTransversoED = len(cache)
    print ( " Contagem de SAMX em transversalED: ", samx_totalTransversoED)
    print ()



    # Abordagem da TRANSVERSAL DIREITA -------------------------------------
    temporaria.clear()
    for linha in range(LINHAS-3):
        # Armazena TRANSVERSA DE na lista 'temporaria'
        for caracter in range(3,COLUNAS):   # Itera entre cada caracter (3 a 136)
            a1 = entrada.at[linha, 0][caracter]
            a2 = entrada.at[linha+1, 0][caracter-1]
            a3 = entrada.at[linha+2, 0][caracter-2]
            a4 = entrada.at[linha+3, 0][caracter-3]
            temporaria.append(a1+a2+a3+a4)
        # Loop
    # Loop
    cache.clear()
    TransversalDE_matriz = df.DataFrame(temporaria)

    # XMAS
    cache = re.findall(xmas_pat, TransversalDE_matriz.to_string())
    xmas_totalTransversoDE = len(cache)
    print (" Contagem de XMAS para transversalDE: ", xmas_totalTransversoDE)
    print ()

    # SAMX
    cache.clear()
    cache = re.findall(inv_xmas_pat, TransversalDE_matriz.to_string())
    samx_totalTransversoDE = len(cache)
    print ( " Contagem de SAMX para transvesalDE: ", samx_totalTransversoDE)
    print ()

    print()
    xmas = xmas_totalLinhas + xmas_totalColunas + xmas_totalTransversoDE + xmas_totalTransversoED
    samx = samx_totalLinhas + samx_totalColunas + samx_totalTransversoDE + samx_totalTransversoED
    soma = xmas + samx

    print (" XMAS: ", xmas, " SAMX: ", samx)
    print ("\tTOTAL: ", soma)

if __name__ == '__main__':
    main()

