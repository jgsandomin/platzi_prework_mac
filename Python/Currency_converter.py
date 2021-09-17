pesos = input ("How many colombian pesos do you have?: ")
pesos = float(pesos)
dolar_value = 3875
dolars = pesos / dolar_value
dolars = round(dolars, 2)
dolars = str(dolars)
print("You have $" + dolars + " dolars")