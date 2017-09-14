contI = 0
soma = 0
media = 0
novaEntrada = str.lower(input("Deseja computar idades: "))
while novaEntrada == "sim":
    idade = int(input("Digite sua idade: "))
    contI +=1
    soma += idade
    media = soma / contI
    novaEntrada = str.lower(input("Deseja computar idades: "))
if media <=25:
    print("A média de idade classifica a turma como JOVEM")
elif media > 25 and media <=60:
    print("A média de idade classifica a turma como ADULTO")
else:
    print("A média de idade classifica a turma como IDOSO")
print("FIM")

    
    
    

    
