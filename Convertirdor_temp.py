# Crear una funcion para convertir de grados celsius a kelvin y viceversa
# Tipo C: de Celsius a Kelvin
# Tipo K: de Kelvin a Celsius

def conversor_temp(grados, tipo):
    if tipo == "C":
        return grados + 273.15
    elif tipo == "K":
        return grados - 273.15
    else:
        return "Error"