aux = 0
pen = 0
ult = 0
num = int(input("Digite um número: "))
for i in range(0, num+1, 1):
    if i == 1:
        ult = 1
    else:
        aux = ult
        ult +=pen
        pen = aux
print("O fibonacci de {} é {}!". format(num, ult))
print("FIM")
        
##QUESTÃO ERRADA:
##Não gera a fibonacci.
