import funciones as fun  # Importa el archivo 'funciones' y lo renombra como 'fun'
import streamlit as st    # Importa la biblioteca Streamlit para crear aplicaciones web

# Título de la barra lateral
st.sidebar.title("Funciones Simples")

# Lista de funciones disponibles en la barra lateral
funcion = st.sidebar.selectbox(
    "Selecciona una función",
    [
        "Saludo",
        "Suma de dos números",
        "Área de un triángulo",
        "Calculadora de descuento",
        "Suma de una lista",
        "Producto con valores predeterminados",
        "Números pares e impares",
        "Multiplicación con *args",
        "Información personal con **kwargs",
        "Calculadora flexible"
    ]
)

# 1. Función de saludo simple:
if funcion == "Saludo":
    nombre = st.text_input("Introduce tu nombre:")  # Solicita al usuario que ingrese su nombre
    if st.button("Saludar"):  # Crea un botón para saludar
        if nombre:  # Verifica si se ingresó un nombre
            st.write(fun.saludar(nombre))  # Llama a la función 'saludar' y muestra el saludo
        else:
            st.write("Por favor, introduce un nombre.")  # Mensaje si no se ingresó un nombre

# 2. Suma de dos números:
elif funcion == "Suma de dos números":
    a = st.number_input("Número 1", value=0)  # Solicita el primer número
    b = st.number_input("Número 2", value=0)  # Solicita el segundo número
    if st.button("Sumar"):  # Crea un botón para sumar
        st.write(f"La suma es: {fun.sumar(a, b)}")  # Muestra el resultado de la suma

# 3. Área de un triángulo:
elif funcion == "Área de un triángulo":
    base = st.number_input("Base", value=0)  # Solicita la base del triángulo
    altura = st.number_input("Altura", value=0)  # Solicita la altura del triángulo
    if st.button("Calcular área"):  # Crea un botón para calcular el área
        st.write(f"El área del triángulo es: {fun.area(base, altura)}")  # Muestra el área calculada

# 4. Calculadora de descuento:
elif funcion == "Calculadora de descuento":
    precio = st.number_input("Precio original", value=0)  # Solicita el precio original
    descuento = st.number_input("Descuento (%)", value=10)  # Solicita el porcentaje de descuento
    impuesto = st.number_input("Impuesto (%)", value=16)  # Solicita el porcentaje de impuesto
    if st.button("Calcular precio final"):  # Crea un botón para calcular el precio final
        st.write(f"El precio final es: {fun.descuento(precio, descuento, impuesto)}")  # Muestra el precio final

# 5. Suma de una lista de números: 
elif funcion == "Suma de una lista":
    numeros = st.text_input("Introduce los números separados por espacios:")  # Solicita números separados por espacios
    if st.button("Sumar lista"):  # Crea un botón para sumar la lista
        try:
            lista_num = list(map(int, numeros.strip().split()))  # Convierte la entrada en una lista de enteros
            st.write(f"La suma de la lista es: {fun.sumar_lista(lista_num)}")  # Muestra la suma de la lista
        except ValueError:  # Maneja el error si hay un valor no válido
            st.write("Asegúrate de que todos los números sean válidos y estén separados por espacios.")

# 6. Funciones con valores predeterminados:
elif funcion == "Producto con valores predeterminados":
    nombre_producto = st.text_input("Nombre del producto:")  # Solicita el nombre del producto
    cantidad = st.number_input("Cantidad", value=1)  # Solicita la cantidad (predeterminada en 1)
    precio = st.number_input("Precio por unidad", value=10)  # Solicita el precio por unidad (predeterminado en 10)
    if st.button("Calcular precio total"):  # Crea un botón para calcular el precio total
        st.write(f"El precio total a pagar es: {fun.producto(nombre_producto, cantidad, precio)}")  # Muestra el precio total

# 7. Números pares e impares:
elif funcion == "Números pares e impares":
    numeros = st.text_input("Introduce los números separados por espacios:")  # Solicita números separados por espacios
    if st.button("Separar pares e impares"):  # Crea un botón para separar pares e impares
        try:
            numeros_lista = list(map(int, numeros.strip().split()))  # Convierte la entrada en una lista de enteros
            if numeros_lista:  # Verifica si la lista no está vacía
                pares, impares = fun.pares(numeros_lista)  # Llama a la función para separar pares e impares
                st.write(f"Números pares: {pares}")  # Muestra los números pares
                st.write(f"Números impares: {impares}")  # Muestra los números impares
            else:
                st.write("No has introducido ningún número válido.")  # Mensaje si la lista está vacía
                
        except ValueError:  # Maneja el error si hay un valor no válido
            st.write("Asegúrate de que todos los números sean válidos y estén separados por espacios.")

# 8. Multiplicación con *args:
elif funcion == "Multiplicación con *args":
    numeros = st.text_input("Introduce los números separados por espacios:")  # Solicita números separados por espacios
    if st.button("Multiplicar"):  # Crea un botón para multiplicar
        try:
            numeros_lista = list(map(int, numeros.split()))  # Convierte la entrada en una lista de enteros
            st.write(f"El resultado de la multiplicación es: {fun.mult_args(*numeros_lista)}")  # Muestra el resultado de la multiplicación
        except ValueError:  # Maneja el error si hay un valor no válido
            st.write("Asegúrate de que todos los números sean válidos y estén separados por espacios.")

# 9. Información de una persona con **kwargs:
elif funcion == "Información personal con **kwargs":
    Nombre = st.text_input("Nombre:")  # Solicita el nombre
    Edad = st.number_input("Edad:", value=0)  # Solicita la edad (predeterminada en 0)
    Direccion = st.text_input("Dirección:")  # Solicita la dirección
    if st.button("Mostrar información"):  # Crea un botón para mostrar la información
        info = fun.inf_personal(Nombre=Nombre, Edad=Edad, Direccion=Direccion)  # Llama a la función para obtener la información
        for clave, valor in info.items():  # Itera sobre la información y la muestra
            st.write(f"{clave}: {valor}")

# 10. Calculadora flexible:
elif funcion == "Calculadora flexible":
    num1 = st.number_input("Número 1", value=0)  # Solicita el primer número
    num2 = st.number_input("Número 2", value=0)  # Solicita el segundo número
    operacion = st.selectbox("Operación", ["suma", "resta", "multiplicación", "división"])  # Solicita la operación a realizar
    if st.button("Calcular"):  # Crea un botón para calcular
        st.write(f"El resultado es: {fun.calculadora_flexible(num1, num2, operacion)}")  # Muestra el resultado de la operación
