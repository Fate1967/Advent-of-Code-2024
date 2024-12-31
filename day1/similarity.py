import pandas as pd

def main():
    arquivo = pd.read_fwf('lista_cmp', widths=[5, 8], header=None)
    lista1 = arquivo[0].copy()
    lista2 = arquivo[1].copy()
    soma = 0
    for _ in lista1:
        for value in lista2:
            if (_ == value):
                soma += value
                print (value)

    print (soma)

if __name__ == '__main__':
    main()


'''
resultado = 0
indice = 0
for _ in lista1:
    resultado += abs(int(lista1[indice] - lista2[indice]))
    indice += 1

print ("Soma = ", resultado)




for index, row in arquivo.iterrows():
    arquivo.loc[index, 'Distancia'] = abs(int (row[1] - row[0]))

distancias = arquivo['Distancia'].sum()

print (distancias)
'''