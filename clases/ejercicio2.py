# IMPORTAR TODAS LAS FUNCIONES DE LA LIBRERÍA SYMPY
import math

from sympy import *
# Visualización de resultados en forma de ecuación:
# Utilizará Látex para la escritura de fórmulas, si no se tiene látex, por defecto se usa MathJax
from sympy.interactive import printing

printing.init_printing(use_latex=True)

# Imprimir línea vacía para espaciar fórmulas
def lin():
  print('\n') # imprime línea vacía

def main2():
    x=symbols('x')
    y=Function('y')

    ecuacion=Eq(diff(y,x)*sin(x),y*ln(y))
    ecuacion1=diff(y,x)*sin(x)-y*ln(y)

    solucion=dsolve(ecuacion1,y(x))

    ci={y(pi/2):math.e()}

    
    
    

    print('============ ENUNCIADO =============')
    lin()
    pprint(ecuacion)
    lin()
    print('============ SOLUCION =============')
    lin()
    pprint(solucion)
    lin()
    print('=================================')
    


if __name__=='__main__':
    main2()