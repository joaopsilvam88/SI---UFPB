num = int(input("Digite um valor: "))
aux = 1
for i in range(num, 1, -1):
    aux *=i
print(" {} ! = {}". format(num, aux))
print("FIM")
