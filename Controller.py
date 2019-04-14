#Farm simulator
#By Ted Ferguson

from Model_Classes import Farm
import os
import string


def print_main_menu():  ## Menu
    print(30 * "-", "MENU", 30 * "-")
    print("1. Check out the Farm")
    print("2. Do work on the Farm")
    print("3. Go to the market")
    print(67 * "-")


name = input("What do you want to name your farm?")

#Farm(name, 10)
#Myanimal = Farm.animals[0]
#Myanimal.eat()

loop = True

while loop:  ## While loop
    print_main_menu()  ## Displays menu
    choice = int(input("Choose wisely\n:"))

    if choice == 1:
        os.system('clear')
        print("Checking out the Farm")
        #Farm.check
    elif choice == 2:
        print("What work do you want to do?")
        ## You can add your code or functions here
    elif choice == 3:
        print("Going to the market")
        ## You can add your code or functions here
        loop = False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Wrong option selection. Enter any key to try again..")
