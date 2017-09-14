horasTrab = int(input("Quantas horas você trabalhou: "))
salarioB= 5*horasTrab
if salarioB <= 900:
    print("Isento")
elif salarioB > 900 and salarioB <= 1500:
    descontIr = salarioB * 0.05
elif salarioB > 1500 and salarioB <=2500:
    descontIr = salarioB * 0.10
else:
    descontIr = salarioB * 0.20
descontInss = salarioB * 0.10
descontFgts = salarioB * 0.11
descontSind = salarioB * 0.03
descontSalario = descontIr + descontInss
salarioL = salarioB - descontSalario
print("O seu salário bruto é de R$ %.2f, todavia..." %salarioB)
print("Haverá um desconto de R$ %.2f refente ao imposto de renda" %descontIr)
print("Haverá um desconto de R$ %.2f refente ao INSS" %descontInss)
print("O sindicato ira receber da empresa em relação ao salário do empregado R$ %.2f" %descontSind)
print("O FGTS ira receber da empresa em relação ao salário do empregado R$ %.2f" %descontFgts)
print("Enfim, o salário líquido do empregado será de R$ %.2f" %salarioL)
print("FIM")

