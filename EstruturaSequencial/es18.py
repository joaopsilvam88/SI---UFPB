tamanhoArq = float(input("Quantos MB tem o arquivo a baixar: "))
velocidadeD = float(input("Qual a velociade de um link de internet em Mbps: ")) 
tempoD = (tamanhoArq / velocidadeD) / 60
print("O tempo do download do seu arquivo será de %.2f minuto(s)" %tempoD)
print("FIM")
    
 ####Só uma conferida nisso, são grandezas diferentes, Megabytes(MB) e Megabits(Mb). Megabytes são um conjunto de 8 Megabits.   
