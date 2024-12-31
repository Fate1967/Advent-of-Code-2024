import pandas as pd
import math




# ************************************************************************** AT LEAST
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

def atLeast(row: list) -> list:
    # Regra: adjacent levels differ by at least one
    # Não deve haver duplicatas

    posicao_anomalias = atLeastFast(row)
    nr_de_anomalias = len(posicao_anomalias)

    if (nr_de_anomalias == 0):
        print ("\tAt Least passou: ", row, "\n")
        return row
    
    else:
        print (" Na linha ", row, ", há valores repetidos nas posições ", posicao_anomalias)

        # If dampener disponivel
        if (main.dampener_used == 0):
            # Passa pelas hipóteses de remoção, ou seja
            # retira o elemento anômalo de todas as posições possíveis
            # e compara novamente.
            # A função toda deve retornar uma row atualizada para a 
            # testagem do próximo critério
            for e in range(nr_de_anomalias):
                
                posicao = posicao_anomalias[e]
                # Guarda elemento em destaque
                temp = row[posicao]

                print (" Vou aplicar o Dampener no elemento ", temp, " na posicao ", posicao, ", e conferir o resultado final ...")
                del row[posicao]
                row_dampener_aplicado = atLeastFast(row)

                if (len(row_dampener_aplicado) == 0):
                    print (" Dampener funcionou para atLeast com o resultado: ", row)
                    main.dampener_used = 1
                    return row
                else: 
                    print (" Dampener falhou em atLeast com a linha modificada: ", row)             
                # Retorna row para sua composição original
                row.insert(posicao, temp)

                # Tentar com elemento da outra posição (posicao -1)                
                print (" Falhou! Então vou aplicar o Dampener no elemento ", temp, " na posicao ", posicao-1, ", e verificar o resultado ...")
                temp = row[posicao-1]
                del row[posicao-1]
                row_dampener_aplicado = atLeastFast(row)

                if (len(row_dampener_aplicado) == 0):
                    print (" Dampener funcionou para atLeast com o resultado: ", row)
                    main.dampener_used = 1
                    return row
                else: 
                    print (" Dampener falhou em atLeast com a linha modificada: ", row)             
                    print (" Falha definitiva com 2 hipóteses eliminadas - 'Insecure'")
                    row.clear()
                    return row
            # Loop          
        # Se não há dampeners disponiveis
        else: 
            print (" Não há dampeners disponíveis(atLeast), resultado permanece:", row)       
        
        # Após passar por todo o processamento: 'row'
        # Então FOI DETECTADA UMA ANOMALIA
        #       FOI TENTADO O DAMPENER
        #       O DAMPENER FALHOU
        #       É Inseguro !
        print (" Linha insegura: ", row.clear())
        return row







    
# ************************************************************************** ORDER
def orderFast(row: list) -> str:
    # Aqui tem que mudar para a idéia de comparação entre lista original e lista ordenada
    size = len(row)
    # ORDEM ASCENDENTE
    for i in range(size):
        if (i > 0):
            if (row[i] > row[i-1]):
                ordem = 'a'
            else:
                ordem = 'f'
                break
    # Loop

    if (ordem == 'a'):
        return ordem
    
    
    # ORDEM DESCENDENTE
    for i in range(size):
        if (i > 0):
            if (row[i] < row[i-1]):
                ordem = 'd'
            else:
                ordem = 'f'
                break
    # Loop

    return ordem

def order(row: list) -> list:   
    # Regra: The levels are either all increasing or all decreasing
    
    size = len(row)
    if (size == 0):
        print (" Já definida como ' Insecure '") 
        return row
    
    ordem = orderFast(row)      # 'd' , 'a' ou 'f'
    print (" Ordem: ", ordem)
    
    if (ordem == 'a'):
        return row

    if (ordem == 'd'):
        return row
        
    if (ordem == 'f'):
        print (" Há uma discrepância na ordem dos elementos")
        print (" Vou tentar usar o Dampener ...")
        if (main.dampener_used == 0):

            # Ordem descendente
            # O elemento da direita não pode ser maior do que o da esquerda
            for i in range(size):
                if (i > 0):
                    if (row[i] > row[i-1]):

                        # Cobrir ambas hipóteses  
                        print ("\n\n DEBUG:\n Original: ", row, "\n\n indice: ", i)


                        # Hipótese 1 - 'i'
                        temp = row[i]
                        row.remove(row[i])
                        print (" Hipótese 1(i) Linha modificada:", row, " Removido: ", temp)
                        # Testa novamente
                        ordem = orderFast(row)
                        if (ordem == 'd'):
                            main.dampener_used = 1
                            print (" Dampener funcionou com 'order' ", ordem) 
                            return row
                        elif (ordem == 'a'):
                            main.dampener_used = 1
                            print (" Dampener funcionou com 'order': ", ordem)
                            return row
                        
                        print (" Hipótese DESCENDENTE 1(i) falhou com valor: ", ordem)

                        # Retornar row a forma original
                        row.insert(i, temp)
                        print ("\n\t Retorna ao original: ", row, "\n")

                        # Hipótese 2 - 'i-1'                        
                        temp = row[i-1]
                        row.remove(row[i-1])
                        print (" Hipótese 2(i-1) Linha modificada:", row, " Removido: ", temp)
                        # Testa novamente
                        ordem = orderFast(row)
                        if (ordem == 'd'):
                            main.dampener_used = 1
                            print (" Dampener funcionou com 'order' ", ordem)                             
                            return row
                        elif (ordem == 'a'):
                            main.dampener_used = 1
                            print (" Dampener funcionou com 'order: ", ordem)
                            return row
                        
                        print (" Hipótese DESCENDENTE 2(i-1) falhou com valor: ", ordem)
                        print (" Falha definitiva, dampener falhor em 'order' - ' Insecure '")
                        row.clear()
                        return row    
            # Loop
        # if dampener
    return row







# ************************************************************************** AT MOST
# at most three
# Verifica se há elementos que atendam ao critério
#  e retorna uma lista com seus índices
def atMostFast(row: list) -> list:
    size = len(row)
    l = []
    for i in range(size):
        if (i > 0):
            if ( abs(row[i] - row[i-1]) > 3 ):
                l.append(i)
                # 'i' jamais será 0
    # Loop
    return l

def atMost(row: list) -> bool:
    # Regra: adjacent levels differ by at most three

    size = len(row)
    if (size == 0):
        print (" Já definida como ' Insecure '") 
        return False  # Linha já definida por critério anterior como ' Insecure '
                    # row está vazia

    posicao_anomalias = atMostFast(row)         # retorna uma lista com os índices das anomalias
                                                # Nunca vai apontar para um índice 0
    nr_de_anomalias = len(posicao_anomalias)    # Nr de ocorrências da anomalia
    print (" Detectadas ", nr_de_anomalias, " anomalias em ", posicao_anomalias)

    # PASSOU POR ATMOST
    if (nr_de_anomalias == 0):
        print ("\tAt Most passou: ", row, "\n")
        return True

    # ANOMALIAS ATMOST DETECTADAS    
    else:
        print (" Na linha ", row, ", há exceções 'atMost' nos valores com índices ", posicao_anomalias)
        print (" Foi usado ", main.dampener_used, " damperes")

        # If dampener disponível
        if (main.dampener_used == 0):
            
            # Hipóteses de remoção ...
            for e in range(nr_de_anomalias):
                
                posicao = posicao_anomalias[e]
                # Guarda elemento em destaque
                temp = row[posicao]

                print (" Vou aplicar o Dampener no elemento ", temp, " na posicao ", posicao, ", e conferir o resultado final ...")
                del row[posicao]
                row_dampener_aplicado = atMostFast(row)
                
                if (len(row_dampener_aplicado)==0):
                    print (" Dampener funcionou para atMost com o resultado: ", row)
                    main.dampener_used = 1
                    return True      
                else:   
                    print (" Dampener falhou em atMost com a linha modificada: ", row)

                row.insert(posicao, temp)


                # ----------------------------------------------------------------------------------------------------------------    
                # Tentar com elemento da outra posição

                # Guarda elemento em destaque
                temp = row[posicao-1]
                print (" Vou aplicar o Dampener no elemento ", temp, " na posicao ", posicao-1, ", e conferir o resultado final ...")
                del row[posicao-1]
                row_dampener_aplicado = atMostFast(row)
                
                if (len(row_dampener_aplicado)==0):
                    print (" Dampener funcionou para atMost com o resultado: ", row)
                    main.dampener_used = 1
                    return True       
                else:   
                    print (" Dampener falhou em atMost com a linha modificada: ", row)
                    print (" Falha definitiva, dampener para atMost não pôde ser aplicado - 'Insecure'")
                    return False
            # Loop
        # Se dampener não disponível retorna row não modificada
        else:
            print (" Não há dampeners disponíveis(atMost), resultado permanece:", row)

        # Após passar por todo o processamento: 'row'
        # Então FOI DETECTADA UMA ANOMALIA
        #       FOI TENTADO O DAMPENER
        #       O DAMPENER FALHOU
        #       Inseguro !
        print (" Passa todo processamento com status: ANOMALIA true, DAMPENER usado e falhado")
        return False
 





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
        # Início por duplicatas > Regra: adjacent levels differ by at least one
        print ("\n\tMEMÓRIA: ", memoria)
        
        # Memória DEVE ser atualizada após ser DAMPEADA
        print (" Todos critérios processados com os seguintes resultados: \n" )

        if (atMost( order( atLeast(memoria) ) )):
            contador += 1
            print ("\n\tMemória: ", memoria, " SAFE\n")
        else:
            print ("\n\tMemória: ", memoria, " Insecure\n")

        memoria.clear()
        mem.clear()

        print (" Dampener usado = ", main.dampener_used)
        main.dampener_used = 0
    # Loop

    print ("------------------------------------------------------------------------------")
    print ("\t\tRESULTADO é ", contador)
    print ("------------------------------------------------------------------------------\n")

if __name__ == '__main__':
    main()

