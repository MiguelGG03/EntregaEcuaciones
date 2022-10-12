import sympy

def main1():
    # Resolviendo ecuación diferencial
    # defino las incognitas
    x = sympy.Symbol('x')
    y = sympy.Function('y')

    # expreso la ecuacion
    f = 6*x**2 - 3*x**2*(y(x))
    sympy.Eq(y(x).diff(x), f)

    # Resolviendo la ecuación
    sympy.dsolve(y(x).diff(x) - f)

if __name__=='__main__':
    main1()