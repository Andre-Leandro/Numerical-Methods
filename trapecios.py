from sympy import symbols, diff

def reglaTrapecio(a, b, f, n):
    x = symbols('x')
    h = (b - a) / n
    resultado = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        resultado += f(a + i * h)
    resultado *= h

    segundaDerivada = diff(f(x), x, 2)

    puntoEvaluacion = (a + b) / 2
    valor_segunda_derivada = segundaDerivada.subs(x, puntoEvaluacion)

    error = -((b - a) * h**2 / 12) * valor_segunda_derivada

    return resultado, error 

def f(x):
    return -x**2 + 6*x - 4

a = 1
b = 4
n = 3

aproximacionIntegral, e = reglaTrapecio(a, b, f, n)
print("Aproximación de la integral:", aproximacionIntegral, "con un error de: ", e)
