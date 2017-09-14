excesso = 0
multa = 0
pesca = int(input("Quantos quilos de peixe pescados: "))
if pesca < 50:
    print(excesso)
    print(multa)
cont = pesca - 50
while pesca > 50 and cont > 0:
    cont -=1
    excesso +=1
    multa +=4
    print("Sua carga excedeu o limite em {} unidades e vai pagar R${}!". format(excesso, multa))
print("FIM")
