"""
Fecha: 01/11/2022
Autor: Roxanyffer Velasco Contreras
Computación Paralela y Distribuida
Principal: Llama a ambos programas Cy/Py
"""

from distutils.core import setup
import POrbita_CY
import POrbita_PY
import time

#Se inicializa el planeta para Python
planet_py = POrbita_PY.Planet()
planet_py.x = 100*10**3
planet_py.y = 300*10**3
planet_py.z = 700*10**3
planet_py.vx = 2.000*10**3
planet_py.vy = 29.87*10**3
planet_py.vz = 0.034*10**3
planet_py.m = 5.97424*10**24

#Se inicializa el planeta para Cython
planet_cy = POrbita_CY.Planet()
planet_cy.x = 100*10**3
planet_cy.y = 300*10**3
planet_cy.z = 700*10**3
planet_cy.vx = 2.000*10**3
planet_cy.vy = 29.87*10**3
planet_cy.vz = 0.034*10**3
planet_cy.m = 5.97424*10**24

#Se consideran las otras variables
time_frame = 400
steps = 2000000

#Definición de experimentos
#Reducción ruido Gaussiano

#Se crea un formato para la impresión sobre el fichero
formato_datos = "{:.5f},{:5f},\n"

for i in range(8):

#Toma de tiempos para Python
    init_time=time.time()
    POrbita_PY.step_time(planet_py, time_frame, steps)
    end_time=time.time()

    time_python = end_time - init_time

#Toma de tiempos para Cython
    init_time=time.time()
    POrbita_CY.step_time(planet_cy, time_frame, steps)
    end_time=time.time()

    time_cython = end_time - init_time

    with open("planeta.csv", "a") as archivo:
        archivo.write(formato_datos.format(time_python, time_cython))

archivo.close()

print("Tiempo de ejecucion con Python: {}s\n".format(time_python))
print("Tiempo de ejcucion con Cython: {}s\n".format(time_cython))

print("Cython es {} veces más rápido que Python ".format(round(time_python/time_cython, 2)))
