def reglaTrapecioTabla(x, y):
    n = len(x) - 1
    h = (x[-1] - x[0]) / n
    resultado = 0.5 * (y[0] + y[-1])

    for i in range(1, n):
        resultado += y[i]
    resultado *= h
   
    return resultado

x_valores = [1, 1.1, 1.2, 1.3, 1.4]
y_valores = [0.010, 0.252, 0.586, 1.024, 1.578]

aproximacionIntegral= reglaTrapecioTabla(x_valores, y_valores)

print("Aproximación de la integral:", aproximacionIntegral)

