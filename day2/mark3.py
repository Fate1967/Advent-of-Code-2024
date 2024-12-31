import pandas as pd
import math
from difflib import ndiff






# ------------------------------------------------------------------------------------------------------------------------------
#                                            NO MÁXIMO TRÊS ...
# ------------------------------------------------------------------------------------------------------------------------------
# at most three
# Verifica se há elementos que atendam ao critério
#  e retorna um inteiro, índice da anomalia 'row[i]'
# retorna 0 se Passou, ou seja, SEM atMost anomalias
def atMostFast(row: list) -> int:
    for i in range(len(row)):
        if (i > 0):
            if ( abs(row[i] - row[i-1]) > 3 ):
                return i
                # 'i' jamais será 0
    # Loop
    return 0

def atMostMain(row:list) -> bool:
        # Regra: adjacent levels differ by at most three

    size = len(row)
    if (size == 0):
        print (" Já definida como ' Insecure '") 
        return False    # Linha já definida por critério anterior como ' Insecure '
                        # row está vazia

    posicao_anomalia = atMostFast(row)          # Retorna um índice da anomalia
                                                # Nunca vai apontar para um índice 0
    # PASSOU POR ATMOST
    if (posicao_anomalia == 0):
        print ("\tAt Most passou: ", row, "\n")
        return True

    # ANOMALIAS ATMOST DETECTADAS    
    else:
        print (" Anomalia detectada em ", posicao_anomalia, ", na linha: ", row)
        # If dampener disponível
        if (main.dampener_used == 0):
            
            # Hipóteses de remoção são i e i-1
                
            # i 
            temp = row[posicao_anomalia]

            print (" Vou aplicar o Dampener no elemento ", temp, ", e conferir o resultado final ...")
            del row[posicao_anomalia]
            
            if (atMostFast(row)==0):
                # Teste nos demais critérios
                if (testeD(row)):
                    print (" PASSOU atMost: ", row)
                    main.dampener_used = 1
                    return True
            row.insert(posicao_anomalia, temp)

            # i - 1
            temp = row[posicao_anomalia-1]

            print (" Vou aplicar o Dampener no elemento ", temp, ", e conferir o resultado final ...")
            del row[posicao_anomalia-1]
            
            if (atMostFast(row)==0):
                # Testa os outros critérios
                if (testeD(row)):
                    print (" PASSOU atMost com dampener: ", row)
                    main.dampener_used = 1
                    return True

        else:        
            print (" Dampener não disponível, row permanece com anomalia ...")
    # Retorno padrão para a função atMostMain(row:list)->bool:
    return False
# ------------------------------------------------------------------------------------------------------------------------------









# ------------------------------------------------------------------------------------------------------------------------------
#                                            PELO MENOS UM ...
# ------------------------------------------------------------------------------------------------------------------------------
# Verifica se há duplicação de elementos
#  e retorna uma lista de suas posições
def atLeastFast(row: list) -> list:
    size = len(row)
    l = []
    for i in range(size):
        if (row.count(row[i]) > 1):
            l.append(i)
    # Loop
    return l

# Nova rotina atLeast 
def atLeastMain(row: list) -> bool:
    cache = []
    l = []
    l = atLeastFast(row)
    atLeastFlag = False

    if (len(l)==0):
        return True
    
    print ("\t* DUPLICATAS(atLeast) em : ", l)  
    print (" Foram usados: ", main.dampener_used, " dampener(es)")
    
    if (main.dampener_used == 0):
    
        print (" Inicia isolamento das hipóteses ...")
        for e in l:
            cache.append(row[e])
            del row[e]
            print (" A row corrigida (hipótese ", e , " ) é ", row)

            # Executa testeD(); se passar ótimo
            if (testeD(row)):
                # Dampener
                main.dampener_used = 1
                print (" PASSOU ")
                return True
            print (" NÃO PASSOU")    
            # Se não passou: segue adiante registro da operação no cache
            row.insert(e, cache[0])
            print (" Row retorna a sua configuração de origem > ", row)
            cache.clear()
    print ("\n\tDUPLICATAS: NÃO PASSOU ")
    return False
# ------------------------------------------------------------------------------------------------------------------------------












# ------------------------------------------------------------------------------------------------------------------------------
#                                            ORDEM ASCENDENTE OU DESCENDENTE ...
# ------------------------------------------------------------------------------------------------------------------------------
# Verifica se a ordem dos elementos é ascendente ou descendente
#  e retorna 'a' se a row estiver em ordem ascendente, 'd' ordem descendente e 'f' para fora de ordem
def orderFast(row: list) -> str:
    copia = row.copy()

    # Ascendente
    copia.sort()
    if (row == copia): return 'a'
    # Descendente
    copia.sort(reverse=True)
    if (row == copia): return 'd'

    return 'f'

def anomaliaOrdem(row: list) -> bool:
    
    size = len(row)
    print (" Analisando ...")
                    
    print ("\n Ordem ascendente suposta ... ...")
    for i in range(size):
        if (i>0):

            if (row[i] < row[i-1]):
                print (" Quebrou ordem 'a' aqui: ", i)
                print ( " Vou tentar o dampener ... ...")
                temp = row[i]
                del row[i]
                if (testeD(row)): 
                    main.dampener_used = 1
                    return True
                row.insert(i, temp)

                temp = row[i-1]
                del row[i-1]
                if (testeD(row)):
                    main.dampener_used = 1
                    return True
                row.insert(i-1, temp)
    # Loop
    print (" Falhou ordem 'a'")

    print ("\n Ordem descendente suposta ... ...")
    for i in range(size):
            
        if (i>0):
            if (row[i] > row[i-1]):
                print (" Quebrou ordem 'd' aqui: ", i)
                print (" Vou tentar o dampener ... ...")
                temp = row[i]
                del row[i]
                if (testeD(row)): 
                    main.dampener_used = 1
                    return True
                row.insert(i, temp)
                
                temp = row[i-1]
                del row[i-1]
                if (testeD(row)):
                    main.dampener_used = 1
                    return True
                row.insert(i-1, temp)

    # Loop
    print (" Falhou ordem 'd'")       
        
    # return padrão para anomaliaOrdem(row: list)->bool
    print (" NÃO PASSOU ordem com dampener")
    return False

def orderMain(row: list) -> bool:   
    # Regra: The levels are either all increasing or all decreasing
    
    size = len(row)
    if (size == 0):
        print (" NÃO PASSOU ") 
        return False
    
    ordem = orderFast(row)      # 'd' , 'a' ou 'f'
    print ("\n\t* ORDENAMENTO DOS ELEMENTOS(order)\n Ordem: ", ordem)
    
    if (ordem == 'a'):
        print (" PASSOU ") 
        return True

    if (ordem == 'd'):
        print (" PASSOU ") 
        return True
        
    if (ordem == 'f'):
        print (" Há uma discrepância na ordem dos elementos")
        # Oportunidade de row ser SAFE
        if (main.dampener_used == 0):
            return anomaliaOrdem(row)
        else: print (" Não há dampener disponível, row permanece com anomalia")

    print (" NÃO PASSOU ") 
    return False
# ------------------------------------------------------------------------------------------------------------------------------










# ------------------------------------------------------------------------------------------------------------------------------
#                                            TESTE RÁPIDO PARA OS CRITÉRIOS
# ------------------------------------------------------------------------------------------------------------------------------
# Teste definitivo; meio rápido e definitivo de averiguar se a row é 'SAFE' 
# Usado nas rotinas de avaliação de hipóteses
def testeD(row: list) -> bool:

    l = len(atLeastFast(row))

    ordem = orderFast(row)
    if (ordem == 'a' or ordem == 'd'):
        ord = True
    else: 
        ord = False

    m = atMostFast(row)

    if (l==0 and ord and m==0): return True
    
    return False
# ------------------------------------------------------------------------------------------------------------------------------









# ------------------------------------------------------------------------------------------------------------------------------
#                                            É SEGURO ? Função central para o processamento de ROW
# ------------------------------------------------------------------------------------------------------------------------------
# Isola o processamento da ROW
def isSafe(row) -> bool:

    # Dá inicio ao processo de verificação de critérios  
    if( atLeastMain(row) ):
        if( orderMain(row) ):
            if ( atMostMain(row) ):
                print (" ", row, " é 'SAFE'")
                return True
    # retorno default para isSafe(row: list) -> bool:
    print ("\n\t", row, " é 'Insegura'")
    return False
# ------------------------------------------------------------------------------------------------------------------------------











            # -------------------------------------------------------------------------------
            #                               *** MAIN ***
            # -------------------------------------------------------------------------------

def main() -> None:
    entrada = pd.read_csv('input.txt', sep=' ', header=None, engine='python')
    #entrada = pd.read_csv('maisTeste', sep=' ', header=None, engine='python')
    #entrada = pd.read_csv('teste', sep=' ', header=None, engine='python')
    mem = []
    memoria = []

    # Inicia variável global para acompanhar o uso do Dampener
    if not hasattr(main, "dampener_used"):
        main.dampener_used = 0
        print ("\n------------------------------------------------------------------------------")
        print ("\t\tINICIANDO PARSER\n")
        print (" Dampener disponível, valor: ", main.dampener_used, "\n")

    # Contador Geral
    nr_geral = 0

    # Contador de ocorrências 'is Safe'
    contador = 0


    print (" Criação da memória ...\n")
    for linha in entrada.iterrows():
        nr_geral += 1
        # Cria 'linha' de trabalho > 'memoria'
        for a in linha[1]:
            mem.append(a)
            memoria = [int(x) for x in mem if math.isnan(x)==False]
        # Loop


        print("\n\n\t\tIniciando LOOP", nr_geral)
        # Verificar critérios de 'Safe' e 'Insecure'
        # Início por duplicatas , Regra: adjacent levels differ by at least one
        print ("\n\tMEMÓRIA: ", memoria)
        
        # Memória DEVE ser atualizada após ser DAMPEADA
        # Row resultante deve voltar ao início do filtro 'SAFE'
        print ("\n\tIniciando processamento, aguarde os resultados: \n" )

        # True , True e True são os indicadores de 'SAFE'
        
        if (isSafe(memoria)):
            contador += 1

        memoria.clear()
        mem.clear()

        print (" Dampener usado: ", main.dampener_used)
        main.dampener_used = 0
    # Loop
    # Loop: for linha in entrada.iterrows()

    print ("------------------------------------------------------------------------------")
    print ("\t\tRESULTADO é ", contador)
    print ("------------------------------------------------------------------------------\n")

if __name__ == '__main__':
    main()

