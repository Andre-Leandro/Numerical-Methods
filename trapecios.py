from sympy import symbols, diff

def reglaTrapecio(a, b, funcion, n):
    h = (b - a) / n
    resultado = 0.5 * (funcion(a) + funcion(b))

    for i in range(1, n):
        resultado += funcion(a + i * h)
    resultado *= h



    segundaDerivada = diff(f, 2)

    valor_segunda_derivada = segundaDerivada.subs(((b-a)/2))

    error = -((b-a) * h**2 / 12) * (f(b) - 2 * f(a) + f(a + h))


    return resultado

def f(x):
    return -x**2 + 6*x - 4

a = 1
b = 4
n = 6  

aproximacionIntegral = reglaTrapecio(a, b, f, n)
print("Aproximación de la integral:", aproximacionIntegral)
