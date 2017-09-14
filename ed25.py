contTrue = 0
contFalse = 0
a = input("Telefonou para a vítima: ")
if a == "sim":
    contTrue +=1
elif a == "não":
    contFalse +=1
b = input("Esteve no local do crime: ")
if b == "sim":
    contTrue +=1
elif b == "não":
    contFalse +=1
c = input("Mora perto da vítima: ")
if c == "sim":
    contTrue +=1
elif c == "não":
    contFalse +=1
d = input("Devia para a vítima: ")
if d == "sim":
    contTrue +=1
elif d == "não":
    contFalse +=1
e = input("Já trabalhou com a vítima: ")
if e == "sim":
    contTrue +=1
elif e == "não":
    contFalse +=1
if contTrue == 2:
    print("Você é considerado como suspeito!")
elif contTrue == 3 or contTrue == 4:
    print("Você é considerado como cúmplice!")
elif contTrue == 5:
    print("Você é considerado como assasino!")
else:
    print("Você é considerado como inocente!")
print("FIM")
