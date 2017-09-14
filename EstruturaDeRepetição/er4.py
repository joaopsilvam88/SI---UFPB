a = int(input("Digite o valor da popolação da cidade A: "))
b = int(input("Digite o valor da popolação da cidade B: "))
anos = 0
while a <= b:
    a *=1.03
    b *=1.015
    anos +=1
print("O tempo em que a população A irá ultrapassar a B é de {} anos!". format(anos))
print("FIM")
