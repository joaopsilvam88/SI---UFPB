nome = str.lower(input("Digite seu nome: "))
maisNotas = "sim"
maiorNota = 0
menorNota = 1000000
soma = 0
cont = 0
while maisNotas == "sim":
    nota = float(input("Digite sua nota: "))
    maisNotas = str.lower(input("Deseja acrescentar mais notas: "))
    soma += nota
    cont +=1
    if nota > maiorNota:
        maiorNota = nota
    elif nota < menorNota:
        menorNota = nota
media = soma/cont
print("Atleta: {}". format(nome))
print("Maior nota: {}". format(maiorNota))
print("Menor nota: {}". format(menorNota))
print("Media das notas: %.2f" %media)
print("FIM")

    
