ladoUm = int(input("Digite o primeiro lado do triângulo: "))
ladoDois = int(input("Digite o segundo lado do triângulo: "))
ladoTres = int(input("Digite o terceiro lado do triângulo: "))
if ladoUm >= 0 or ladoDois >= 0 or ladoTres >= 0:
    print("Podemos formar um triângulo...")
    if ladoUm == ladoDois and ladoDois == ladoTres:
        print("O triângulo é do tipo equilátero")
    elif ((ladoUm == ladoDois) or (ladoDois == ladoTres) or (ladoTres == ladoUm)):
        print("O triângulo é do tipo isóceles")
    else:
        print("O triângulo é do tipo escaleno")
else:
    print("Não podemos formar um triângulo!")
