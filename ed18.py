dia = int(input("Digite um número correspondente ao dia: "))
mes = int(input("Digite um número correspondente ao mes: "))
ano = int(input("Digite um número correspondente ao ano: "))
if dia > 31 or mes > 12:
    print("Formato de data inválido!")
else:
    print("{} / {} / {}". format(dia, mes, ano))
print("FIM")
