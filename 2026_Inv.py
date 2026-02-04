#es un comentario de una línea
print(f"Hola mundo desde Python") #esto es un comentario
'''
es comentario de mas de una
línea, sirve para documentar funcions, clases y demas
'''

x = 5
print(x)
#type es una función nativa de PY que muestra el tipo de dato de una variable
print(type(x))

x = "Juan"
print(x)
print(type(x))

apellido = 'Perez'
nombre = "Luis"
cedula = '231325648'
sueldo = 500.57
# sql = 'insert into persona values (\'Luis\', \'Perez\')'


print(apellido)
print(nombre)
print(cedula)
print(sueldo)
print(type(sueldo))

x = 5.3
y = int(x)
print(y)

z = "5"
d = int(z)
print(d)
print(type(d))

print("saludos " + nombre + " "+ apellido)
print(f"Saludos {nombre} {apellido}")


v = True
f = False
print(v)
print(f)
print(type(v))
print(type(f))

print(6>6)

valor_a = 15
valor_b = 4
suma = valor_a + valor_b
print(suma)
print(type(suma))

resta = valor_a - valor_b
print(resta)
print(type(resta))

mult = valor_a * valor_b
print(mult)
print(type(mult))

div = valor_a / valor_b
print(div)
print(type(div))

mod = valor_a % valor_b
print(mod)
print(type(mod))


edad = 5
print(f'Es mayor de edad: {edad >= 0 and edad < 18}')
