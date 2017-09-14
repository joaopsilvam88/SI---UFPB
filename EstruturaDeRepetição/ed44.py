votoJunior = 1
votoVanessa = 2
votoPenha = 3
votoSara = 4
votoNulo = 5
votoBranco = 6
contJ = 0
contV = 0
contP = 0
contS = 0
contN = 0
contB = 0
contTotal = 0
voto = str.lower(input("Deseja votar: "))
while voto == "sim":
    contTotal +=1
    codigo = str.lower(input("Qual opção de voto você quer escolher (um, dois, três, quatro, cinco ou seis): "))
    if codigo == "um":
        contJ +=1
    elif codigo == "dois":
        contV +=1
    elif codigo == "três":
        contP +=1
    elif codigo == "quatro":
        contS +=1
    elif codigo == "cinco":
        contN +=1
    elif codigo == "seis":
        contB +=1
    voto = str.lower(input("Deseja votar: "))
percentNulo = (contN / contTotal) * 100
percentBranco = (contB / contTotal) * 100
print("O total de votos para Junior foi de {}". format(contJ))
print("O total de votos para Vanessa foi de {}". format(contV))
print("O total de votos para Penha foi de {}". format(contP))
print("O total de votos para Sara foi de {}". format(contS))
print("O total de votos Nulos foi de {}". format(contN))
print("O total de votos Brancos foi de {}". format(contB))
print("O percentual de votos nulos foi de {}%". format(percentNulo))
print("O percentual de votos brancos foi de {}%". format(percentBranco))


  
  
    
