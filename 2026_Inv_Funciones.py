def calcular_area(figura, ancho, alto):
    '''
    Esta función calcula el area de la figura y el ancho de la alto
    :param figura: puede ser cuadrado, rectangulo, triangulo
    :param ancho: valor del ancho en numero positivos
    :param alto: valor del alto en numero positivos
    :return: una cadena de texto con el calculo del area correspondiente al figura
    '''
    figura_revisada = figura.lower().strip()
    area = 1
    if figura_revisada == 'cuadrado' or figura_revisada == 'rectangulo':
        area =  alto * ancho
    elif figura_revisada == 'triangulo':
        area = (alto * alto)/2
    else:
        figura_revisada = 'Opcion ivalida'
    return f'El area de la {figura_revisada} es {area}'

print(calcular_area('Cuadrado   ', 5, 5))
print(calcular_area('trianulo', 5, 8))
print(calcular_area('triangulo', 5, 8))

print(calcular_area(alto=4,ancho=5, figura='rectangulo'))