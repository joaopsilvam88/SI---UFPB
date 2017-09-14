notaUm = float(input("Digite sua nota: "))
notaDois = float(input("Digite sua outra nota: "))
media = (notaUm + notaDois) / 2
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
print("FIM")
