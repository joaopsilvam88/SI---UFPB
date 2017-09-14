area = int(input("Digite o valor da área que será pintada: "))
litros = area//6
temp = 0

quantL = litros//18
aux = litros%18
if aux > 0:
    quantL +=1

quantG = litros // 3.6
aux = litros%3.6
if aux > 0:
    quantG +=1

quantGEXTRA = 0
litros = (area // 6) * 1.1
quantLEXTRA = litros // 18
aux = litros%18

if aux > 0:
    quantLEXTRA +=1
    temp = aux // 3.6
    if temp > 0:
        quantGEXTRA +=1
print("Você irá comprar {} lata(s), pagando um total de R$ {}". format(quantL, quantL * 80))
print("Você irá comprar {} galão(galões), pagando um total de R$ {}". format(quantG, quantG * 25))
print("Você irá comprar {} lata(s) e {} galão(galões), pagando um total de R$ {}". format(quantLEXTRA, quantGEXTRA, (quantLEXTRA * 80) + (quantGEXTRA * 25)))
        

    
    
