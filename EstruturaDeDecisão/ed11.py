salario = float(input("Digite seu salário: "))
if salario <= 280:
    porcent =  salario * 0.20
    aumento = porcent + salario
    print("Você ganhava R$ %.2f, mas..." %salario)
    print("Seu salario ganhou um aumento de 20%")
    print("O valor do aumento é de R$ %.2f" %porcent)
    print("Então, seu novo salário ficou em R$ %.2f" %aumento)
elif salario > 280 and salario <= 700:
    porcent = salario * 0.15
    aumento = porcent + salario    
    print("Você ganhava R$ %.2f, mas..." %salario)
    print("Seu salario ganhou um aumento de 15%")
    print("O valor do aumento é de R$ %.2f" %porcent)
    print("Então, seu novo salário ficou em R$ %.2f" %aumento)
elif salario > 700 and salario <= 1500:
    porcent = salario * 0.10
    aumento = porcent + salario
    print("Você ganhava R$ %.2f, mas..." %salario)
    print("Seu salario ganhou um aumento de 10%")
    print("O valor do aumento é de R$ %.2f" %porcent)
    print("Então, seu novo salário ficou em R$ %.2f" %aumento)
else:
    porcent = salario * 0.05
    aumento = porcent + salario    
    print("Você ganhava R$ %.2f, mas..." %salario)
    print("Seu salario ganhou um aumento de 5%")
    print("O valor do aumento é de R$ %.2f" %porcent)
    print("Então, seu novo salário ficou em R$ %.2f" %aumento)
print("FIM")


    
