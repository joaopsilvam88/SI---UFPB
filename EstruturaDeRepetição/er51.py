n = 1
m = 1
fracoes = "sim"
auxM = 0
auxN = 0
while fracoes == "sim":
    x = int(input("Digite um numero: "))
    fracoes = str.lower(input("Deseja realizar mais somas de frações: "))
    for i in range(1, x+1):
        n += 1
        m += 2
    auxM = m + 1
    auxN = n + 1
print("O acumulado das frações é {} / {}". format(auxN, auxM))
