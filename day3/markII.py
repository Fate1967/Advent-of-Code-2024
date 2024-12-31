import re

# Cores
class cor:
    HEADER = '\33[95m'
    OKBLUE = '\33[94m'
    OKCYAN = '\33[96m'
    OKGREEN = '\33[92m'
    WARNING = '\33[93m'
    FAIL = '\33[91m'
    ENDC = '\33[0m'
    BOLD = '\33[1m'
    UNDERLINE = '\33[4m'

MULSIZE = 8         # Para não usar 'números mágicos' no código
                    # É o menor len possível para mul ' mul(x,y) '
                    # O maior é 12 ' mul(xxx,yyy) '
    

# ------------------------------------------------------------------
# Analisa e resume o conjunto de 
# dados, a uma lista de expressões válidas
def analisaDados(data: list) -> list:
    # Armazena resultados
    dadosA = []
    # Padrões
    # REGEX para mul(d1, d2), do() e don't()
    mul_pattern = r'mul\(\d{1,3},\d{1,3}\)'
    dont_pattern = r'don\'t\(\)'
    do_pattern = r'do\(\)'

    print ("\n\t\t INICIANDO LOOP \n")


    # Loop Principal
    while (len(data)>MULSIZE):
        # Enquanto houverem dados, vou continuar
        print ("\n Len(data): ", len(data))

        # Qual a próxima ocorrência de dont ?
        # data será amostrada de acordo com essa ocorrência
        if (re.search(dont_pattern, data)):
            dont_start, dont_end = re.search(dont_pattern, data).span()
        else:
            # E se não houver mais dont a frente ?
            dont_end = len(data)

        print (" dont_end: ", dont_end)

            
        # Pego uma amostra dos dados para o trabalho
        # data -> list é preservada
        amostra = data[:dont_end]
        print (" Loop: Len(amostra): ", len(amostra))

        # Enquanto houver expressões na amostra
        while (re.search(mul_pattern, amostra)):

            mul_start, mul_end = re.search(mul_pattern, amostra).span()
            # Adiciono expressões válidas a dadosA
            dadosA.append( amostra[mul_start:mul_end] )
            print (" Amostra válida armazenada: ", amostra[mul_start:mul_end])
            # Corta da amostra, os dados já armazenados
            amostra = amostra[mul_end:]
        # Loop

        print (" Processada a amostra e armazenadas as expressões válidas")
        # Atualiza data, cortando os valores já trabalhados
        # primeiro: onde dont termina > toda entrada cessa
        # segundo: onde está o primeiro do() > entrada reinicia

        data = data[dont_end:]
        # Foi cortado de data tudo que já foi processado

        
        # Próxima ocorrências de do()
        if (re.search(do_pattern, data)):
            do_start, do_end = re.search(do_pattern, data).span()
        else:
            do_end = len(data)

        print (" do_end: ", do_end)
        # Foram cortados os dados após dont()
        data = data[do_end:]
        print (" Atualizados os dados em 'data'")         
    # Loop
    
    return dadosA

# Multiplica os valores
def multiplica(mul: str) -> int:
    padrao = r'\d{1,3}'
    valor = re.findall(padrao, mul) 
    return (int(valor[0]) * int(valor[1]))


# ------------------------------------------------------------------
# Retorna o texto do arquivo de trabalho
def parse_text(file_path) -> str:
    # Lê o texto do arquivo
    with open(file_path, 'r', encoding='utf-8') as file:
        dados = file.read()     
    return dados


# ------------------------------------------------------------------
#                            * MAIN *
# ------------------------------------------------------------------

def main():
    # Caminho para o arquivo de texto
    file_path = "input"

    # Parseia o texto e cria o DataFrame
    dados = parse_text(file_path)


    # Preencha a lista com expressões 'mul' válidas 
    # para o contexto DESEJADO
    
    # expressoesValidas = preencheExpressoes(dados)

    mulValidas = analisaDados(dados)

    # Multiplica e soma
    resultado = 0

    for mul in mulValidas:
        valor_mul = multiplica(mul)
        print (mul, " - ", valor_mul)
        resultado += valor_mul
    # Loop

    print (" O resultado final é: "+ cor.OKGREEN, resultado)
    print (cor.ENDC)

if __name__ == '__main__':
    main()