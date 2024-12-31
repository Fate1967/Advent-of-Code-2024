import pandas as pd

def problemDampener(indice: int, serie: list, memoria: list, ordem: str) -> bool:

    if (main.has_called == 0):

        # Testa novamente

        if (ordem == 'a' or ordem == 'd'):
            
            # Elimina elemento problemático
            serie[1].pop(indice-1)
            memoria.pop(indice-1)

            if (ordem == 'a'):
                main.has_called = 1
                # Ordem ascendente
                c = 0
                for a in serie[1]:
                    # Pula primeiro 'a'
                    if (c > 0):
                        if (memoria[c-1] >= a):
                            return False
                    c +=1
                return True
        
            else:
                main.has_called = 1
                # Ordem descendente
                c = 0
                for a in serie[1]:
                    # Pula primeiro 'a'
                    if (c > 0):
                        if (memoria[c-1] <= a):
                            return False
                    c +=1
                return True
        
        elif (ordem == 'l'):
            main.has_called += 1

            # Elimina elemento problemático
            #serie[1].remove(a)
            memoria.remove(indice)

            # Ainda há duplicatas ?
            for a in serie[1]:
                if(a):    
                    if (memoria.count(a) > 1):
                        return False
            return True
    return False    

def testaOrdem(serie: list, memoria: list) ->bool:

    # Ordem ascendente
    c = 0
    for a in serie[1]:
        # Pula primeiro 'a'
        if (c > 0):
            if (memoria[c-1] >= a):
                # Problem dampener
                if (problemDampener(c, serie, memoria, 'a')):
                    return True

                # Verifica ordem descendente
                c = 0
                for a in serie[1]:
                    # Pula primeiro 'a'
                    if (c > 0):
                        if (memoria[c-1] <= a):
                            # Problem dampener
                            return (problemDampener(c, serie, memoria, 'd'))
                        c += 1
                return True
        c += 1
    # Loop
    return False

def ordem(serie: list, memoria: list) -> bool:
    flag = testaOrdem(serie, memoria)    
    if (flag): 
        return True
    else:
        print ("ordem falhou")
        return False

# Maior diferença 3
def atMost(serie: list, memoria: list) -> bool:
    c = 0
    for a in serie[1]:
        # Pular o primeiro 'a'
        if (c > 0):
            if (abs((memoria[c-1]-a)) > 3):
                print("atMost falhou")
                return False
        c += 1
    return True

# Menor diferença 1. Há duplicatas? Mais de uma?
def atLeast(serie: list, memoria: list) -> bool:
    
    # Há duplicatas ?
    for a in serie[1]:
        if (a):
            if (memoria.count(a) > 1):
                flag = True
                # Aciona Dampener
                return problemDampener(int(a), serie, memoria, ordem='l')
    # Loop

    return True

# Todos critérios 'True' para emitir 'Safe'
def checaCriterios(serie: list, memoria: list) -> bool:
    main.has_called = 0
    if (atLeast(serie, memoria)  and atMost(serie, memoria) and ordem(serie, memoria)):
        return "Safe"
    else:
        return "Insecure"


def main() -> None:

    if not hasattr(main, "has_called"):
        main.has_called = 0

    data = pd.read_csv('input.txt', sep='/s+', header=None, engine='python')
    #data = pd.read_csv('maisTeste', delim_whitespace=True, header=None)
    #data = pd.read_csv('teste', delim_whitespace=True, header=None)
    memoria = []
    contagem = 0

    # Loop principal
    # Itera entre as linhas de dados(serie) do INPUT
    for serie in data.iterrows():

        # Cria e carrega uma memoria com os valores da serie 
        for a in serie[1]:
            memoria.append(a)

        # Checa se os critérios foram satisfeitos
        # Retorna 'Safe' ou 'Insecure'
        Diagnostico = checaCriterios(serie, memoria)
        
        # Armazena os resultados 'Safe' em um contador
        if (Diagnostico == "Safe"):
            contagem += 1
    
        # Imprime RELATÓRIO
        # Usa 'memoria' para melhor visualização
        # Pode usar 'serie[1]'
        print (memoria, Diagnostico)
        print('-----')

        # Limpa a memória da serie, liberando para a próxima linha de dados
        memoria.clear()
    # Loop

    # Apresenta resultado FINAL    
    print ("A contagem final foi ", contagem)

    #  ***  FIM   ***
if __name__ == '__main__':
    main()
