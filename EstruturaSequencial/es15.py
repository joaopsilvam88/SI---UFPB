ganhoHora = float(input("Qual seu faturamento por hora: "))
horasMes = int(input("Quantas horas trabalhadas no mês: "))
salarioB = ganhoHora * horasMes
ir = salarioB * 0.11
inss = salarioB * 0.08
sind = salarioB * 0.05
descont = ir + inss + sind
salarioL = salarioB - descont
print("O que você deveria ganhar é R$ %.2f, porém..." %salarioB)
print("R$ %.2f foram descontados para o imposto de renda" %ir)
print("R$ %.2f foram descontados para o INSS" %inss)
print("R$ %.2f foram descontados para o sindicato" %sind)
print("O total descontado foi de R$ %.2f" %descont)
print("E o seu salário líquido ficou em R$ %.2f" %salarioL)
print("FIM")










