# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:46:30 2019
@author: Jorge Baltodano Quispe
IDE: Spyder
Facebook : https://www.facebook.com/CodeOrange01/
"""

#Vamos a comenzar con cadenas inmutables, aquellas como: cadenas, tuplas y bytes.


#%%%

""" > Cadenas y Bytes"""
#Los datos textuales en python se manejan con "str" cadenas.

#1. Cadenas con comillas simples para albergar cadenas cortas
cadenaSimple='Esto es una cadena, es corta'
cadenaSimple
#salida: 'Esto es una cadena, es corta'

#2. Cadenas con comillas dobles para albergar cadenas de longitud considerable
cadenaDoble="Esto es una cadena, con comillas dobles para texto algo mas extenso"
cadenaDoble
#Salida: "Esto es una cadena, con comillas dobles para texto algo mas extenso"

#3. Cadenas con collias tripes, para albergar cadenas de varias lineas.

cadenaTriple=""" Esto es una cadena, que engloba  contenido de varias lineas
es muy utilizado para almacenar url o cuando se trabaja con textminning,
es por ello que es muy importante su uso"""
cadenaTriple

#Para saber el tamaño de una cadena:
len(cadenaTriple)

#%%
""" >Codificacion de decodificacion de cadenas."""

# Usando los metodos (se hablará de metodos en los siguientes apartados) encode / decode, se puede codificar las cadenas en objetos de byte utilizando la codificacion UTF-8 que es la dominante para la web 


#Utilizando el encode
s= "Esto es un unícóde  # "
type(s)

encode_s = s.encode('utf-8')
encode_s

#type(encode_s)

#Utilizando en decode

encode_s.decode('utf-8')


#%%

""" >Cadenas de indexacion y Corte"""

""" 1-La indexacion es acceder a un elemento dentro de una cadena por su poscion"""

cadena= "Esto es una cadena de elementos letras."

#Acceder a una de las letras de la cadena, letra "c"
cadena[12]
 #Salida : c
 
 #Acceder a letra "e"
cadena[0]
 #Salida : "E"

""""2.El corte(slit) es una metodo de corte que obtiene una subcadea de la cadena """

# cadena= "Esto es una  cadena de elementos letras."
          #0123456789101112........................

#2.1. Obtener una subcadena de las 7 primeras letras, tener en cuenta que python se cuenta desde 0 y que los espacios tambien son posiciones, ademas si se desea los 7 elementos primero se debe posicionar un valor mas, osea hasta el indice 8 para que se pueda incluir lo que se desea.

cadena[0:8]
# Salida:'Esto es '

#Otra forma para el ejercicio anterior seria

cadena[:8]
#salida: 'Esto es '


#2.2. Obtener una cadena con los 7 ultimas letras de la cadena

cadena[-7:]
 #Salida: 'letras.'
 
 #Otra forma seria
cadena[31:]
 

#2.3. Otra forma de recorrer una cadena es utilizando start-stop-step

cadena[1:27:3]
#Salida: 's  aandem'
 #1: representa inicio del recorrido
 #27: Fin del recorrido
 #3: recorre cada tres indices(1,3,6,9,etc..)


""" Formao de cadenas""" 
#Vamos aprender a formatear las cadenas para utilizarlas como plantillas.

#1.Reemplazando cadenas con %s

cadena="Hola %s , un placer conocerte."
nombre=" Lorenzo"

cadena % nombre
  # Salida: "Hola Lorenzo, un placer conocerte."

#2.Reemplazando con {} {} por posiciones
persona= "Hola {} {}, {}!"
persona.format("Jorge","Baltodano","placer conocerte.")
  #Salida: 'Hola Jorge Baltodano, placer conocerte.!'

#3. Reemplazando por las posiciones e idx.
person="Hola,{0}!, {1}, {2},nos vemos {0}"
person.format("Jorge Baltodano","un placer conocerte","Gracias por su visita")
    #Salida: 'Hola,Jorge Baltodano!, un placer conocerte, Gracias por su visita,nos vemos Jorge Baltodano'


#%%

""" TUPLAS """

#Otro tipo de datos inmutable son las tuplas, que es una secuencia de objetos arbitrarios en python.
t=() # Definiendo una tupla vacía
type(t) #Tipo tuple

#1.Tupla que almacena datos separados por comas
DatosCliente=("Jorge","Baltodano","Quispe",18, "M",1.80,"caucasico","Ing.Sistemas")
DatosCliente[:]

#2. Tupla puede contener otra tupla
DatosEmpleado=("Nombres",("Jorge","Baltodano"),"Cargos",("Ing.Sistemas","Tecnico Informatico"))
DatosEmpleado[:2]

#3. Utilizar el elemento "in" para buscar un aracter o cadena

"Baltodano" in DatosCliente
 #Salida: True




