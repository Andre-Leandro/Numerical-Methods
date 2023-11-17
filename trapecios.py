from sympy import symbols, diff, Abs

def reglaTrapecio(a, b, f, n):
    x = symbols('x')
    h = (b - a) / n
    resultado = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        resultado += f(a + i * h)
    resultado *= h

    segundaDerivada = diff(f(x), x, 2)

    puntoEvaluacion = (a + b) / 2
    valorSegundaDerivada = segundaDerivada.subs(x, puntoEvaluacion)

    error = Abs(-((b - a) * h**2 / 12) * valorSegundaDerivada)

    return resultado, error 

def f(x):
    return 1 + x**3
a = 0
b = 2
n = 10

aproximacionIntegral, e = reglaTrapecio(a, b, f, n)
print("Aproximación de la integral:", aproximacionIntegral, "con un error de: ", e)
