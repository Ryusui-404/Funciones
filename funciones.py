def saludar(nombre):
    return f"Hola, {nombre}"

def sumar(a, b):
    return a + b

def area(base, altura):
    return (base * altura) / 2

def descuento(precio, descuento=10, iva=16):
    precio_descuento = precio - (precio * descuento / 100)
    precio_final = precio_descuento + (precio * iva / 100)
    return precio_final

def sumar_lista(numeros):
    return sum(numeros)

def producto(producto, cantidad=1, precio=10):
    return cantidad * precio

def pares(numeros):
    pares = []
    impares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

def mult_args(*nums):
    resultado = 1
    for num in nums:
        resultado *= num
    return resultado if nums else 1

def inf_personal(**datos):
    return datos

def calculadora_flexible(num1, num2, operacion="suma"):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicación":
        return num1 * num2
    elif operacion == "división":
        if num2 == 0:
            return "Error: División por cero"
        else:
            return num1 / num2
    else:
        return "Operación inválida"