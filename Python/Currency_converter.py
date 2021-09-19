def converter(currency_type, dollar_value):
    pesos = input ("How many" + currency_type + "do you have?: ")
    pesos = float(pesos)
    dolars = pesos / dollar_value
    dolars = round(dolars, 2)
    dolars = str(dolars)
    print("You have $" + dolars + " dolars")

menu = """"

This is a currency conversor 

1 - Colombian pesos
2 - Agentine pesos
3 - Mexican pesos

Please select an option

"""

option = int(input(menu))

if option == 1:
    converter("colombianos",3875)
elif option == 2:
    converter("argentinos",98)
elif option == 3:
    converter("mexicanos",24)
else:
    print ("Enter a valid option")
