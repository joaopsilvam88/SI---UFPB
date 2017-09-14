c = 0
d = 0
u = 0
num = int(input("Digite um número: "))
if num <=1000:
    c = num//100%100
    d = num//10%100
    u = num//1%10
    print("{} centena(s), {} dezena(s) e {} unidade(s)". format(c, d, u))
else:
    print("Número inválido!")
print("FIM")
    
