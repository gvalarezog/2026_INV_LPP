'''
Las listas van entre [] y son ordenadas, se pueden cambiar y permite duplicados
'''
# lista = [3, 'cuatro', True, 5.5]
# print(lista[2])
# lista.append(False)
# print(lista)
# lista.remove(5.5)
# print(lista)
# lista.pop()
# print(lista)
# lista.pop()
# print(lista)
# # print(lista[2])
# lista[0] = 10
# print(lista)

'''
Las tuplas van entre () y son ordenas y no se pueden cambiar
'''
# tupla = (3, 'cuatro', True, 5.5)
# print(tupla)
# # tupla.append(False)
# # tupla.pop()
# # tupla.remove(5.5)
# print(tupla[1])
'''
El conjunto va entre {}, no tiene orden, no se puede repetir los elementos
'''
# conjuto = {'uva', 'pera', 'higo'}
# print(conjuto)
# conjuto.add('naranja')
# print(conjuto)
# conjuto.remove('naranja')
# print(conjuto)
# conjuto.add('uva ')
# print(conjuto)
'''
Diccionario va entre {} pero un elemento corresponde a la llave y el valor
d = {'llave':valor, 'llave2':valor2}'}
'''
# dicc = {'nombre':'Guillermo', 'edad':25, 'color':'amarillo'}
# print(dicc)
#
# print(dicc['edad'])
# dicc['edad'] = 35
# print(dicc)


# number = -1
# if number > 0:
#     print("The number is positive")
# print(f'esta es una nueva linea dentro del if cuando la condición es True')

# number = 8
# if number > 10:
#     print("The number is positive")
#     print(f'esta es una nueva linea dentro del if cuando la condición es True')
# elif number > 0:
#     print("The number es menor que 10")


# lista = [3, 'cuatro', True, 5.5]
# for item in lista:
#     print(item)

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print('Salio del ciclo While')