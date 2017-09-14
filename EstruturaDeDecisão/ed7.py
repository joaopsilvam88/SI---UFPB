numUm = int(input("Digite um número: "))
numDois = int(input("Digite um número: "))
numTres = int(input("Digite um número: "))
if numUm > numDois and numDois > numTres:
    print("O maior número é {} e o menor é {}". format(numUm, numTres))
elif numUm < numDois and numDois < numTres:
    print("O maior número é {} e o menor é {}". format(numTres, numUm))
elif numUm > numTres and numTres > numDois:
    print("O maior número é {} e o menor é {}". format(numUm, numDois))
elif numUm < numTres and numTres < numDois:
    print("O maior número é {} e o menor é {}". format(numDois, numUm))
elif numTres > numUm and numUm > numDois:
    print("O maior número é {} e o menor é {}". format(numTres, numDois))
else:
    print("O maior número é {} e o menor é {}". format(numDois, numTres))
print("FIM")



          
