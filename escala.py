"""
Programa para determinar la escala de un mapa
utilizando la formula

1/E = ab/AB

Donde:
1 Unidad en el mapa, generalmente un cm
E Escala
ab Distancia gráfica entre dos puntos del mapa(cm o milímetros)
AB Distancia real entre dos puntos (mts o Km)
by Raiza(rafaalonso0110@gmail.com) 12/08/2021
"""
from formula import *
print("Determina la escala de un mapa")
opcion = 1
while opcion != 0:
    print("1: Conocer la escala de un mapa")
    print("2: Conocer la distancia gráfica")
    print("3: Conocer la distancia real")
    print("0: Salir del programa")
    print("")
    opcion = input("Selecciona la opción de deseas calcular: ")
    if opcion == "1":
        escala()
    elif opcion == "2":
        distancia_grafica()
    elif opcion == "3":
        distancia_real()
    elif opcion == "0":
        print("Hasta pronto")
        opcion = 0
    
