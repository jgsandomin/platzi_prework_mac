import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un numero entre el 1 y el 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Elige un número mayor')
        else:
            print('Eige un número menor')
        numero_elegido = int(input('Elige otro número: '))
    print('Ganaste!')


if __name__ == '__main__':
    run()