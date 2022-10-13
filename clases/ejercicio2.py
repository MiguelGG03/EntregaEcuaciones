# IMPORTAR TODAS LAS FUNCIONES DE LA LIBRERÍA SYMPY
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

    ecuacion=diff(y,x)*sin(x)-y*ln(y)
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
    main2()