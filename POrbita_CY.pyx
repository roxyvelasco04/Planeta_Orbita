cimport cython

#cython: language_level=3
"""
Fecha: 01/11/2022
Autor: Roxanyffer Velasco Contreras
Computación Paralela y Distribuida

"""

import cython_builtins
from math import sqrt

"""
Se requiere la raíz cuadrada:
Se instancia como función externa
"""

cdef extern from "math.h":
        double sqrt(double x) nogil

cdef class Planet(object):
#Variables públicas: declaración
        cdef public float x,y,z,vx,vy,vz,m


        def __init__(self):
        #Posición y velocidad inicial
            self.x = 1.0
            self.y = 0.0
            self.z = 0.0
            self.vx = 0.0
            self.vy = 0.5
            self.vz = 0.0

            self.m = 1.0

"""
Puede ser la distancia 0:
Para evitar lo anterior, preparamos una alerta
basada en Cython: cdivision(True/False):
    Al poner true, invalida la instrucción
    al saltar la bandera (INF).
Se prepara con un decorador de CYTHON
"""

@cython_cdivision(True)
cdef void single_step(Planet planet, double dt):

    cdef double Fx, Fy, Fz, distance


    #Calcular la fuerza
    distance = sqrt(planet.x**2 + planet.y**2 + planet.z**2)
    Fx = -planet.x / distance**3
    Fy = -planet.y / distance**3
    Fz = -planet.z / distance**3

    #Posición de cada iteración
    planet.x += dt * planet.vx
    planet.y += dt * planet.vy
    planet.z += dt * planet.vz

    #Velocidad de cada iteración
    planet.vx += dt * Fx / planet.m
    planet.vy += dt * Fy / planet.m
    planet.vz += dt * Fz / planet.m
 
def step_time(Planet planet, double time_span, int n_steps):
    cdef double dt
    cdef int j
    dt = time_span / n_steps
    """
    Se prepara para paralelismo
    """
    with nogil:
        for j in range(n_steps):
            single_step(planet, dt)

