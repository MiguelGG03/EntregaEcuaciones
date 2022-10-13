from sympy import *
import sympy
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

#que imprima utilizando notacion matematica
sympy.init_printing(use_latex='mathjax')

def main1():
    # Resolviendo ecuación diferencial
    # defino las incognitas
    x = sympy.Symbol('x')
    y = sympy.Function('y')

    # expreso la ecuacion
    f =  ((x**2)*y(x)-y(x))/(y(x)-1)
    enunciado=sympy.Eq(y(x).diff(x), f)

    #expreso la condicion inicial
    ics = {y(3): -1}
    
    # Resolviendo la ecuación
    solucion=sympy.dsolve(y(x).diff(x) - f)

    #Ahora reemplazamos los valores de la condicion inicial en nuestra ecuacion   

    C_eq = sympy.Eq(solucion.lhs.subs(x, 3).subs(ics), solucion.rhs.subs(x, 3))

    solucion_eq=sympy.solve(C_eq)

    print('=============================')
    print('        ENUNCIADO')
    print('=============================\n\n') 
    pprint(enunciado)
    print('\n\n')
    print('=============================')
    print('         SOLUCION')
    print('=============================\n\n') 
    pprint(solucion)
    print('\n\n')
    '''
    print('=============================')
    print(' SOLUCION CON VALOR INICIAL')
    print('=============================\n\n') 
    pprint(solucion_eq)
    print('\n\n')
    '''
if __name__=='__main__':
    
    main1()
    