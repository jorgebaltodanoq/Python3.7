# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:03:24 2019

@author: Jorge Baltodano Quispe
IDE: Spyder
Facebook : https://www.facebook.com/CodeOrange01/

"""

# Lo que aprenderás en esta seccion es acerca de los datos
"""
-Estructuras de objetos de Python
-Mutabilidad e inmutabilidad.
-Tipos de datos incorporados: números, cadenas, secuencias, colecciones y tipos de mapeo
-El módulo de colecciones.
-Enumeraciones

"""

#%%

"""DATOS NUMERICOS:"""

 # Enteros: en Python  los enteros disponen de un rango ilimitado, sujeto a la cantidad de memoria virtual 

a=14
b=3
# Sumando enteros en python

a + b
 
 #Restando enteros en python
a-b
 
 #Multiplicar enteros en python
a * b
 
 #Dividir enteros en python, division decimal
a / b
 
 #Dividir enteros en python, division entera
a//b
 
 #Obtener modulo o resto de una division en python
 
a % b
 
 #Obtener  potencia en python
a** b
 
 

#%%

""" Truncamiento de numeros con python"""

-7 /4
#Resultado es -1.75

-7//4
# Resultado es:-2

#si en el ejemplo dos se esperaba como respuesta -1, es un erro!, en la division entera, siempre se redondea al menos infinito.
#Si desea truncar un numero es de la siguiente manera

int(-1.75)
#Resultado: -1

#%%
""" Legitimidad en Python"""

#otra de las caracteristicas bellas de python es que te permite agregar legitimidad a los numeros, utilizando los "_" en forma de separador:

a=6000000 #Seis millones, aunque por la cercania de los ceros es dificil percatarse.
a

b=6_000_000
b # El resultado es el mismo de salida. Pero facilita al programador



#%%
#Datos Booleanos:
"""en Python : Python maneja los datos booleamos con valores "true" and "false" representan "1" y "0" respectivamente. Ademas se puede utilizar por su valor
"""
# utilizando el dato booleano como true and false

bool(2)
#Salida True 

bool(-42)
#Salida : True

True and True
#Salida True

True and False
#Salida: False


#Utilizar boleanos como numero

1+True
#Salida: 2

3-True
#Salida:2

35* False
#Salida: 0 

#%%
""" Numeros Reales """
#Numeros reales o de punto flotante se representan en python segun el forma flotante de la IEEE 754 que almacena 64 bit dividido en : signo, exponente y mantisa.

pi=3.1415926536  #Ejemlo de numero real
radio=34.2
area = pi * (radio**2)
area
#Salida: 3674.5324313567044


#%%%

""" Numeros Complejos:"""
#Python te da numeros complejos, es decir, numero que se pueden expresar en : a +ib donde a y b son numeros reales e i es la uidad imaginaria, es decir la raiz cuadrada.

c=3.14 + 2.73j
c
#Salida (3.14+2.73j)

#%%

""" Fracciones y Decimales"""
#Las fraciones sostiene un racional numero y un denomidador en sus formas simples. 
from fractions import Fraction
Fraction(10,6)
#salida Fraction(5,3)

Fraction(1,3) + Fraction(2,3) # 1/3 + 2/3 == 3/3==1/1
#salida : Fraction(1,1)

f=Fraction(10,6) # 10/6== 5/3
f.numerator  #Numerador = 5
#Salida:5

f.denominator #Demoninador=3
#Salida: 3


