um = int(input("Digite um número: "))
dois = int(input("Digite outro número: "))
tres = int(input("Digite mais um número: "))
if um > dois and dois > tres:
    print("A ordem descrescente é {}, {}, {}". format(um, dois, tres))
elif tres > dois and dois > um:
    print("A ordem descrescente é {}, {}, {}". format(tres, dois, um))
elif um > tres and tres > dois:
    print("A ordem descrescente é {}, {}, {}". format(um, tres, dois))
elif dois > tres and tres > um:
    print("A ordem descrescente é {}, {}, {}". format(dois, tres, um))
elif tres > um and um > dois:
    print("A ordem descrescente é {}, {}, {}". format(tres, um, dois))
else:
    print("A ordem descrescente é {}, {}, {}". format(dois, um, tres))
print("FIM")
    
          
