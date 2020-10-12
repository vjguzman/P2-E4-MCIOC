# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:53:17 2020

@author: vjguzman
"""

import numpy as np
import itertools

g = 9.81 #kg*m/s^2


class Barra(object):

    """Constructor para una barra"""
    def __init__(self, ni, nj, R, t, E, ρ, σy):
        super(Barra, self).__init__()
        self.ni = ni
        self.nj = nj
        self.R = R
        self.t = t
        self.E = E
        self.ρ = ρ
        self.σy = σy

    def obtener_conectividad(self):
        return [self.ni, self.nj]

    def calcular_area(self):
        A = np.pi*(self.R**2) - np.pi*((self.R-self.t)**2)
        return A

    def calcular_largo(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        xi = reticulado.obtener_coordenada_nodal(self.ni)
        xj = reticulado.obtener_coordenada_nodal(self.nj)
        dij = xi-xj
        return np.sqrt(np.dot(dij,dij))

    def calcular_peso(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        L = self.calcular_largo(reticulado)
        A = self.calcular_area()
        return self.ρ * A * L * g











    def obtener_rigidez(self, ret):
        A = self.calcular_area()
        L = self.calcular_largo(ret)

        xi = ret.obtener_coordenada_nodal(self.ni)
        xj = ret.obtener_coordenada_nodal(self.nj)

        cosθx = (xj[0] - xi[0])/L
        cosθy = (xj[1] - xi[1])/L
        cosθz = (xj[2] - xi[2])/L

        Tθ = np.array([ -cosθx, -cosθy, -cosθz, cosθx, cosθy, cosθz ]).reshape((6,1))

        return self.E * A / L * (Tθ @ Tθ.T )

    def obtener_vector_de_cargas(self, ret):
        W = self.calcular_peso(ret)

        return np.array([0, 0, -W, 0, 0, -W])


    def obtener_fuerza(self, ret):
        ue = np.zeros(6)
        ue[0:3] = ret.obtener_desplazamiento_nodal(self.ni)
        ue[3:] = ret.obtener_desplazamiento_nodal(self.nj)
        
        A = self.calcular_area()
        L = self.calcular_largo(ret)

        xi = ret.obtener_coordenada_nodal(self.ni)
        xj = ret.obtener_coordenada_nodal(self.nj)

        cosθx = (xj[0] - xi[0])/L
        cosθy = (xj[1] - xi[1])/L
        cosθz = (xj[2] - xi[2])/L

        Tθ = np.array([ -cosθx, -cosθy, -cosθz, cosθx, cosθy, cosθz ]).reshape((6,1))

        return self.E * A / L * (Tθ.T @ ue)





    def chequear_diseño(self, Fu, ret, ϕ=0.9):
        """Para la fuerza Fu (proveniente de una combinacion de cargas)
        revisar si esta barra cumple las disposiciones de diseño.
        """
        A = self.calcular_area()
        Fn = A* self.σy
        if  ϕ*Fn < abs(Fu):
            return False
        else:
            return True


    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        """Para la fuerza Fu (proveniente de una combinacion de cargas)
        calcular y devolver el factor de utilización
        """
        A = self.calcular_area()
        Fn = A* self.σy
        
        return abs(Fu/ (ϕ*Fn))


    def rediseñar(self, Fu, ret, ϕ=0.9):
        """Para la fuerza Fu (proveniente de una combinacion de cargas)
        re-calcular el radio y el espesor de la barra de modo que
        se cumplan las disposiciones de diseño lo más cerca posible
        a FU = 1.0.
        """
        #https://drive.google.com/file/d/1J2d-sjMsG8c74wQr3dVFAqJOD-MqnK2o/view
        #min 20:30
        #R = 8*cm => 0,08
        #t = 5*mm => 0.005

        R = np.arange(0.01, 0.09, 0.01)
        T = np.arange(0.001, 0.006, 0.001)

        combis = list(itertools.product(R, T))

        cumple = []
        
        for combi in combis:
            r = combi[0]
            t = combi[1]
            r_t = r-t
            A = np.pi*((r**2)-(r_t**2))
            I = (np.pi/4)*((r**4)-(r_t**4))
            L = self.calcular_largo(ret)
            Rgiro = np.sqrt(I/A)
            i = np.sqrt(L/Rgiro)
            if i <= 300:
                cumple.append(combi)

        cumple_fu = []

        for combi in cumple:
            r = combi[0]
            t = combi[1]
            r_t = r-t
            A = np.pi*((r**2)-(r_t**2))
            I = (np.pi/4)*((r**4)-(r_t**4))
            L = self.calcular_largo(ret)

            if Fu < 0: #compresion
                caso_1 = A*self.σy
                caso_2 = (np.pi**2)*self.E*I/(L**2)
                Fn = min(caso_1,caso_2)
            else: #traccion
                Fn = A*self.σy

            FO = abs(Fu)/(ϕ*Fn)

            if FO < 1:
                cumple_fu.append([r,t,FO])

        valores_fu = []
        for i in cumple_fu:
            valores_fu.append(i[2])
        maximo = max(valores_fu)

        maximos = []
        for i in cumple_fu:
            if i[2] == maximo:
                maximos.append(i)

        self.R = maximos[0][0]
        self.t = maximos[0][1]

        return None