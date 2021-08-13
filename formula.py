def escala():
    ab = int(input("Ingresa la distancia gráfica en cm: "))
    AB = int(input("Ingresa la distancia real en Km: "))
    AB = AB *100000
    escala = (1*AB)/ab
    print("La Escala es 1:",escala)
    print("")

def distancia_grafica():
    E = int(input("Ingresa la escala en cm: "))
    AB = int(input("Ingresa la distancia real en Km: "))
    AB = AB *100000
    ab = (1*AB)/E
    print("La distancia gráfica es: ",ab," cm")
    print("")

def distancia_real():
    E = int(input("Ingresa la escala en cm: "))
    ab = int(input("Ingresa la distancia gráfica en cm: "))
    AB = ((E*ab)/1)/100000
    print("La distancia real es: ",AB, " Km")
    print("")
