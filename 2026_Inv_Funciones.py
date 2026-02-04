def calcular_area(figura, ancho, alto):
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