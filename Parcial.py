# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 18:46:47 2021

@author: Edgar_Polo
"""
print("Inicio Parcial")
# Ejercicio numero 1
precio = int(input('Ingrese el precio por kilos de las manzanas: '))
cantidad = int(input('Ingrese Número de kilos comprados: '))
total = precio * cantidad
Dcto_1 = total * 0.10
Dcto_2 = total * 0.15
Dcto_3 = total * 0.20
print("El valor a descontar es de: ")
if cantidad >= 0 and cantidad < 2:
    print('0%')
if cantidad >= 2 and cantidad < 5:
    print(Dcto_1)
if cantidad >= 5 and cantidad < 10:
    print(Dcto_2)
if cantidad >= 10:
    print(Dcto_3)

# Ejercicio numero 2
precio = int(input('Inserte el valor de los abanicos: '))
cant = int(input('Inserte la cantidad de abanicos comprados: '))
clave = input('Inserte clave de descuento: ')
total = precio * cant
if clave == '010':
    total_con_descuento = total - (total * 0.20)
    print(f' Total: {total_con_descuento}')
elif clave == '020':
    total_con_descuento = total - (total * 0.40)
    print(f' Total: {total_con_descuento}')
elif clave == '030':
    total_con_descuento = total - (total * 0.55)
    print(f' Total: {total_con_descuento}')
elif clave == '040':
    total_con_descuento = total - (total * 0.75)
    print(f' Total: {total_con_descuento}')

# Ejercicio numero 3
precio_Prod = int(input('Ingrese el precio del producto : '))
marca = input('Ingrese la marca del producto: ')
if precio_Prod >= 4000 and marca == 'nosy':
    total_descuento = precio_Prod - (precio_Prod * 0.20) - (precio_Prod * 0.10)
    total_con_iva = total_descuento + (precio_Prod * 0.30)
    print(f' Total: {total_con_iva}')
elif precio_Prod >= 4000:
    total_descuento = precio_Prod - (precio_Prod * 0.20)
    total_con_iva = total_descuento + (precio_Prod * 0.30)
    print(f' Total: {total_con_iva}')
elif marca == 'nosy':
    total_descuento = precio_Prod - (precio_Prod * 0.10)
    total_con_iva = total_descuento + (precio_Prod * 0.30)
    print(f' Total: {total_con_iva}')

# Ejercicio numero 4
No_hectareas = int(input('Ingrese el número de hectáreas del bosque : '))
if No_hectareas > 5:
    pinos = float(No_hectareas * 0.80)
    oyamel = float(No_hectareas * 0.15)
    cedro = float(No_hectareas * 0.05)
    print('Se Deben sembrar')
    print(f'Hectáreas de pinos: {pinos}')
    print(f'Hectáreas de  oyamel: {oyamel}')
    print(f'Hectáreas de cedro: {cedro}')
elif No_hectareas <= 5:
    pinos = float(No_hectareas * 0.45)
    oyamel = float(No_hectareas * 0.25)
    cedro = float(No_hectareas * 0.30)
    print('Se Deben sembrar')
    print(f'Hectáreas de pinos: {pinos}')
    print(f'Hectáreas de  oyamel: {oyamel}')
    print(f'Hectáreas de cedro: {cedro}')

# Ejercicio numero 5
num1 = int(input('Ingrese un número : '))
num2 = int(input('Ingrese un número : '))
num3 = int(input('Ingrese un número : '))
if num1 > num2 and num1 > num3:
    print(f'El mayor numero es el : {num1}')
elif num2 > num1 and num2 > num3:
    print(f'El mayor numero es el : {num2}')
elif num3 > num1 and num3 > num2:
    print(f'El mayor numero es el : {num3}')
