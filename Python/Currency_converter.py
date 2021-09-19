menu = """"

This is a currency conversor 

1 - Colombian pesos
2 - Agentine pesos
3 - Mexican pesos

Please select an option

"""

option = int(input(menu))

if option == 1:
    pesos = input ("How many colombian pesos do you have?: ")
    pesos = float(pesos)
    dolar_value = 3875
    dolars = pesos / dolar_value
    dolars = round(dolars, 2)
    dolars = str(dolars)
    print("You have $" + dolars + " dolars")
elif option == 2:
    pesos = input ("How many argentine pesos do you have?: ")
    pesos = float(pesos)
    dolar_value = 98
    dolars = pesos / dolar_value
    dolars = round(dolars, 2)
    dolars = str(dolars)
    print("You have $" + dolars + " dolars")
elif option == 3:
    pesos = input ("How many mexican pesos do you have?: ")
    pesos = float(pesos)
    dolar_value = 20
    dolars = pesos / dolar_value
    dolars = round(dolars, 2)
    dolars = str(dolars)
    print("You have $" + dolars + " dolars")
else:
    print ("Enter a valid option")
