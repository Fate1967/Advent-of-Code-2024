import pandas as pd

arquivo = pd.read_fwf('lista_cmp', widths=[5,8], header=None)
lista1 = arquivo[0].sort_values(ascending=True, ignore_index=True)
print(lista1)
lista2 = arquivo[1].sort_values(ascending=True, ignore_index=True)
print(lista2)


resultado = 0
indice = 0
for _ in lista1:
    resultado += abs(int(lista1[indice] - lista2[indice]))
    indice += 1

print ("Soma = ", resultado)



'''
for index, row in arquivo.iterrows():
    arquivo.loc[index, 'Distancia'] = abs(int (row[1] - row[0]))

distancias = arquivo['Distancia'].sum()

print (distancias)
'''