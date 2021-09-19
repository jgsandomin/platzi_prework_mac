def conversation(message):
    print("Hello")
    print("How are you?")
    print(message)
    print("Bye!")

option = int(input("Choice an option (1, 2, 3): "))
if option == 1:
    conversation("You chose the option 1")
elif option == 2:
    conversation("You chose the option 2")
elif option == 3:
    conversation("You chose the option 3")
else:
    print("You should select a valid option")