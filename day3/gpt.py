import pandas as pd

def parse_text(file_path):
    # Lê o texto do arquivo
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Lista para armazenar os resultados
    parsed_data = []

    # Processa os caracteres individualmente
    for index, char in enumerate(text):
        # Exemplos de análise
        char_info = {
            'Position': index,
            'Character': char,
            'IsLetter': char.isalpha(),
            'IsDigit': char.isdigit(),
            'IsWhiteSpace': char.isspace(),
            'ASCIIValue': ord(char)
        }
        parsed_data.append(char_info)

    # Cria um DataFrame com os resultados
    df = pd.DataFrame(parsed_data)
    return df
    
def main():
    # Caminho para o arquivo de texto
    file_path = "input"

    # Parseia o texto e cria o DataFrame
    df = parse_text(file_path)

    # Exibe as primeiras linhas do DataFrame
    print (df.head())

    # Exporta os resultados para um arquivo csv
    df.to_csv('parsed.csv', index=False)

    # Análise agregada de exemplo
    print ("\nResumo")
    print (df[['IsLetter', 'IsDigit', 'IsWhiteSpace']].sum())

if __name__ == '__main__':
    main()