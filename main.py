#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Iván Vázquez C.I 24724027
# Laboratorio 1

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

#Trabajo solo con el data set de la clase de matematica
data = pd.read_csv('student-mat.csv', sep=";")

edad = data['age']

#funcion para promedio
def mymean(entrada):
    return float(sum(entrada)) / max(len(entrada), 1)

print 'Edad promedio: ' + str(np.mean(edad))

# --------- Histograma -------------

plt.hist(edad)
plt.title("Histograma de edades")
plt.xlabel("Edades")
plt.ylabel("Frecuencias")
plt.show() # mayormente edades comprendidas entre 15 y 18 años

# -------- Diagrama de dispersión -----------

#Notas del primer lapso vs Notas finales
G1 = data['G1']
G3 = data['G3']
plt.scatter(G1,G3)
plt.title("Diagrama de dispersion")
plt.xlabel("Notas del Lapso 1")
plt.ylabel("Notas del Lapso 3")
plt.show() #Hipotesis: Los alumnos con bajo desempeño en el primer lapso, lo mantuvieron hasta el final.
#Por el contrario, los alumnos con notas altas desde el principio las mantuvieronhasta el tercer lapso.

# ------ 1 ¿Cuál es la nota final promedio de los que más consumo de alcohol tienen?
aux = data[data['Dalc']==5]
print 'Respuesta 1: ' + str(np.mean(aux['G3']));

# ------ 2 ¿Quiénes son más estudiosos, los niños o las niñas?
chicos = data[data['sex']=="M"]
chicas = data[data['sex']=="F"]
print 'Promedio de niños: ' + str(np.mean(chicos['G3']))
print 'Promedio de niñas: ' + str(np.mean(chicas['G3']))
print 'Respuesta 2: Los niños son más estudiosos'

# ------ 3 ¿El noviazgo de los alumnos puede llegar a afectar las horas de estudio por semana?
love = data[data['romantic']=="yes"]
print love
#Histograma de horas de estudio en noviazgo
aux1 = love['studytime']
plt.plot(aux1)
plt.title("Histograma de alumnos con pareja")
plt.xlabel("Horas de estudio")
plt.ylabel("Frecuencias")
plt.show()

#Histograma de horas de estudio en soltería
nolove = data[data['romantic']=="no"]
aux2 = nolove['studytime']
plt.hist(aux2)
plt.title("Histograma de alumnos solteros")
plt.xlabel("Horas de estudio")
plt.ylabel("Frecuencias")
plt.show() #Se observa que los que no tienen pareja son mayoría en dedicarle de 2 a 5 horas al estudio
#mientras que los que sí tienen pareja son menos los que le dedican de 2 a 5 horas al estudio (que es 
#el intervalo recomendado)
print 'Respuesta 3: Sí afecta, justificación en los comentarios'