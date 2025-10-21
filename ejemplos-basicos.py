# -----------------------------------------------
# SESIÓN 2: VARIABLES, TIPOS DE DATOS Y ENTRADA DE DATOS
# -----------------------------------------------
# Autor: (tu nombre)
# Objetivo: Comprender cómo manejar variables, tipos de datos,
# realizar operaciones básicas y capturar información del usuario.
# -----------------------------------------------

# --- 1. CREACIÓN DE VARIABLES Y ASIGNACIÓN DE VALORES ---

print("Hola mundo")

# Ejemplos de diferentes tipos de datos
nombre = "Daniel"
edad = 17
altura = 1.72
es_estudiante = True

# Mostrar los valores en pantalla
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Es estudiante?:", es_estudiante)

# Mostrar el tipo de dato de cada variable
print("\n--- Tipos de datos ---")
print("Tipo de 'nombre':", type(nombre))
print("Tipo de 'edad':", type(edad))
print("Tipo de 'altura':", type(altura))
print("Tipo de 'es_estudiante':", type(es_estudiante))

# --- 2. OPERACIONES BÁSICAS CON NÚMEROS ---

print("\n--- Operaciones básicas ---")
a = 8
b = 3

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)  # división entera
print("a % b =", a % b)    # residuo

# --- 3. OPERACIONES CON TEXTO ---

print("\n--- Operaciones con texto ---")
saludo = "Hola, " + nombre + "!"
print(saludo)
print("Tu nombre tiene", len(nombre), "letras.")

# --- 4. CAPTURA DE DATOS DESDE EL TECLADO ---

print("\n--- Captura de datos ---")
usuario = input("¿Cómo te llamas? ")
edad_usuario = int(input("¿Cuántos años tienes? "))
altura_usuario = float(input("¿Cuál es tu altura en metros? "))

print("\nHola", usuario, "!")
print("Tienes", edad_usuario, "años y mides", altura_usuario, "metros.")

# --- 5. CONVERSIÓN DE TIPOS Y OPERACIONES ---

# Calcular año de nacimiento
anio_actual = 2025
anio_nacimiento = anio_actual - edad_usuario

print("\n--- Cálculos ---")
print("Naciste en el año", anio_nacimiento)

# Calcular edad futura
edad_2030 = 2030 - anio_nacimiento
print("En el año 2030 tendrás", edad_2030, "años.")

# --- 6. DECISIONES SIMPLES ---

print("\n--- Decisión ---")
if edad_usuario >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# --- 7. MINI DESAFÍO FINAL ---
# Programa que calcule el promedio de tres calificaciones

print("\n--- Promedio de calificaciones ---")
c1 = float(input("Calificación 1: "))
c2 = float(input("Calificación 2: "))
c3 = float(input("Calificación 3: "))

promedio = (c1 + c2 + c3) / 3
print("Tu promedio es:", promedio)

if promedio >= 70:
    print("¡Felicidades, aprobaste!")
else:
    print("Lo siento, no aprobaste. Sigue practicando.")
