# Calcular el total de un pago incluyendo impuestos.
# Formula: pago_total = pago_sin_impuestos + pago_sin_impuestos * impuesto

def calcula_impuestos(pago_sin_impuestos, impuesto):
    return pago_sin_impuestos + pago_sin_impuestos * impuesto

print(calcula_impuestos(100, 0.18))