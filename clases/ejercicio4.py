# IMPORTAR TODAS LAS FUNCIONES DE LA LIBRERÍA SYMPY
from sympy import *
# Visualización de resultados en forma de ecuación:
# Utilizará Látex para la escritura de fórmulas, si no se tiene látex, por defecto se usa MathJax
from sympy.interactive import printing

printing.init_printing(use_latex=True)

# Imprimir línea vacía para espaciar fórmulas
def lin():
  print('\n') # imprime línea vacía

def main4():
    t=symbols('t')
    y=Function('y')('t')

    ecuacion=2*t*diff(y,t)-y-3*(t)**2
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
    


if __name__=='__main__':
    main4()