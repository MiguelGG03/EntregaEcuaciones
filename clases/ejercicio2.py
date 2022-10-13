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
    y=Function('y')('x')

    ecuacion1=Eq(diff(y,x)*sin(x),y*ln(y))
    ecuacion=diff(y,x)*sin(x)-y*ln(y)
    solucion=dsolve(ecuacion)
    

    print('============ ENUNCIADO =============')
    lin()
    pprint(ecuacion1)
    lin()
    print('============ SOLUCION =============')
    lin()
    pprint(solucion)
    lin()
    print('=================================')
    print('\nNo he logrado pasarle el \nparametro inicial\ny(3)=-1')
    


if __name__=='__main__':
    main2()