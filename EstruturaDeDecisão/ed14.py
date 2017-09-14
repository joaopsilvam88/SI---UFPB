notaUm = float(input("Digite sua nota: "))
notaDois = float(input("Digite sua outra nota: "))
media = (notaUm + notaDois) / 2
conceitoA = media >= 9 and media <= 10
conceitoB = media >= 7.5 and media <= 9
conceitoC = media >= 6 and media <= 7.5
conceitoD = media >= 4 and media <= 6
conceitoE = media >= 0 and media <= 4
if conceitoA:
    print("Sua primeira nota é %.2f" %notaUm)
    print("Sua segunda nota é %.2f" %notaDois)
    print("Sua média é de %.2f" %media)
    print("Esta média está encaixada no conceito A")
    print("Aprovado!")
if conceitoB:
    print("Sua primeira nota é %.2f" %notaUm)
    print("Sua segunda nota é %.2f" %notaDois)
    print("Sua média é de %.2f" %media)
    print("Esta média está encaixada no conceito B")
    print("Aprovado!")
if conceitoC:
    print("Sua primeira nota é %.2f" %notaUm)
    print("Sua segunda nota é %.2f" %notaDois)
    print("Sua média é de %.2f" %media)
    print("Esta média está encaixada no conceito C")
    print("Aprovado!")
if conceitoD:
    print("Sua primeira nota é %.2f" %notaUm)
    print("Sua segunda nota é %.2f" %notaDois)
    print("Sua média é de %.2f" %media)
    print("Esta média está encaixada no conceito D")
    print("Reprovado!")
elif conceitoE:
    print("Sua primeira nota é %.2f" %notaUm)
    print("Sua segunda nota é %.2f" %notaDois)
    print("Sua média é de %.2f" %media)
    print("Esta média está encaixada no conceito E")
    print("Reprovado!")


