# IMPORTAR TODAS LAS FUNCIONES DE LA LIBRERÍA SYMPY
from sympy import *
# Visualización de resultados en forma de ecuación:
# Utilizará Látex para la escritura de fórmulas, si no se tiene látex, por defecto se usa MathJax
from sympy.interactive import printing

printing.init_printing(use_latex=True)

# Imprimir línea vacía para espaciar fórmulas
def lin():
  print('\n') # imprime línea vacía


def main3():
    t=symbols('t')
    y=Function('y')('t')

    ecuacion=diff(y,t)-(y/(t-2))-2*(t-2)**2
    solucion=dsolve(ecuacion)
    

    print('============ ENUNCIADO =============')
    lin()
    pprint(ecuacion)
    lin()
    print('============ SOLUCION =============')
    lin()
    pprint(solucion)
    lin()
    print('=================================')