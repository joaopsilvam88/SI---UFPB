tamanhoArq = float(input("Quantos MB tem o arquivo a baixar: "))
velocidadeD = float(input("Qual a velociade de um link de internet em Mbps: "))
tempoD = (tamanhoArq / velocidadeD) / 60
print("O tempo do download do seu arquivo será de %.2f minuto(s)" %tempoD)
print("FIM")
    
    
