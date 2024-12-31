import re

# ------------------------------------------------------------------
#                          INÍCIO
# ------------------------------------------------------------------


# ------------------------------------------------------------------
# Retorna o texto do arquivo de trabalho
def parse_text(file_path) -> str:
    # Lê o texto do arquivo
    with open(file_path, 'r', encoding='utf-8') as file:
        dados = file.read()     
    return dados

# Lida com processamento incompleto de dados
def reclamaDados(dados: list) -> list:
    listaResultado = []
    # REGEX para mul(d1, d2)
    mul_pattern = r'mul\(\d{1,3},\d{1,3}\)'

    while (re.search(mul_pattern, dados)):
        mul = re.search(mul_pattern, dados)
        start, end = mul.span()
        listaResultado.append(dados[start:end])
        dados = dados[end:]

    return listaResultado


# Preenche a lista de expressões válidas
# Retorna a lista de expressões mul válidas
def preencheExpressoes(dados: list) -> list:

    # Lista de armazenamento das expressões válidas
    expressoesValidas = []

    # Isola critérios
    # do() e don't   
    # REGEX para mul(d1, d2)
    mul_pattern = r'mul\(\d{1,3},\d{1,3}\)'

    # REGEX para do() e don't()
    dont_pattern = r'don\'t\(\)'
    do_pattern = r'do\(\)'

    # Controle para o loop principal
    while (len(dados)>0):

        mul = re.search(mul_pattern, dados)
        start, end = mul.span()

        do = re.search(do_pattern, dados)
        dont = re.search(dont_pattern, dados)

        if (not dont): # Supostamente não há dont(s) a frente
            expressoesValidas.append(dados[start:end])
            dados = dados[end:]
            expressoesValidas += reclamaDados(dados)
            break
            
        # Armazeno 'mul'
        dont_start, dont_end = dont.span()
        do_start, do_end = do.span()
        
        # Aplicação de critérios
        # Está antes do próximo dont ?
        if (end < dont_start):
            expressoesValidas.append(dados[start:end])
            dados = dados[end:]
        else:
            dados = dados[do_end:]
    # Loop

    # Saída padrao de preencheExpressoes(dados: list) -> list:
    return expressoesValidas




# Multiplica os valores
def multiplica(mul: str) -> int:
    padrao = r'\d{1,3}'
    valor = re.findall(padrao, mul) 
    return (int(valor[0]) * int(valor[1]))

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
    expressoesValidas = preencheExpressoes(dados)

    # Multiplica e soma
    resultado = 0
    for mul in expressoesValidas:
        valor_mul = multiplica(mul)
        print (mul, " - ", valor_mul)
        resultado += valor_mul
    # Loop

    print (" O resultado final é: ", resultado)


if __name__ == '__main__':
    main()