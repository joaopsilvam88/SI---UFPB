maior = 0
menor = 10000
tempT = 0
aux = 0
novaEntrada = "sim"
while novaEntrada == "sim":
    temp = float(input("Digite uma temperatura: "))
    novaEntrada = str.lower(input("Deseja acrescentar mais temperaturas: "))
    aux +=1
    if temp > maior:
        maior = temp
    elif temp < menor:
        menor = temp
    tempT +=temp
media = tempT / aux
print("A maior temperatura é {}º!". format(maior))
print("A menor temperatura é {}º!". format(menor))
print("A média das temperaturas é {}º!". format(media))
print("FIM")
