multUm = 0
multDois = 0
multTres = 0
multQuatro = 0
multCinco = 0
multSeis = 0
multSete = 0
multOito = 0
multNove = 0
multDez = 0
cont = 0
num = int(input("Digite um número: "))
for cont in range(0, 10):
    multUm = num*1
    multDois = num*2
    multTres = num*3
    multQuatro = num*4
    multCinco = num*5
    multSeis = num*6
    multSete = num*7
    multOito = num*8
    multNove = num*9
    multDez = num*10
    cont +=10    
print(multUm)
print(multDois)
print(multTres)
print(multQuatro)
print(multCinco)
print(multSeis)
print(multSete)
print(multOito)
print(multNove)
print(multDez)

##Não está errado, porém o for está inutilizado nesse caso, o que demanda maior processamento (um processamento desnecessário),
##note que se retirar o for o programa funciona da mesma forma.
##A ideia do for na calculadora seria justamente para não atribuir uma variável para cada multiplicação.

    
   
