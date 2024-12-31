import pandas as pd
import re

def parse_text(file_path) -> list:
    
    # Lista para armazenar os resultados
    expressao = []

    # Lê o texto do arquivo
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

        # REGEX para mul(d1, d2)
        padrao = r'mul\(\d{1,3},\d{1,3}\)'

        while (re.search(padrao,text)):
            start, end = re.search(padrao, text).span()
            expressao.append(text[start:end])
            text = text[end:]

    return expressao

def multiplica(mul: str) -> int:
    padrao = r'\d{1,3}'
    valor = re.findall(padrao, mul) 
    return (int(valor[0]) * int(valor[1]))
    
def main():
    # Caminho para o arquivo de texto
    file_path = "input"

    # Parseia o texto e cria o DataFrame
    df = parse_text(file_path)

    # Variáveis de trabalho
    resultado = 0

    # Passa um a um resultado do parser
    for mul in df:  
        print (mul)

        # Multiplica e soma
        resultado += multiplica(mul)
    # Loop""

    print (" O resultado final é: ", resultado)

if __name__ == '__main__':
    main()