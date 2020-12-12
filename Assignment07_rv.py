#-------------------------------------------------#
# Title: Pickling and error handling for music keyboard
# Description: Demonstrates pickling and exception handling in one script
# ChangeLog: (who,when,what)
# rvandercar.12/09/2020.created script for assignment 07
#-------------------------------------------------#

import pickle # dump and load

# Data -------------------------------------------- #
strFileName = 'keyboard_prices.dat'
lstkeyboard = []
dicrow = {}
keyboard = ''
price = ''
# Processing -------------------------------------- #
class Processor:
    @staticmethod
    def adding_data(keyboard, price, list_of_keys):
        dicrow = {"keyboard": keyboard, "price": price}
        list_of_keys.append(dicrow)
        print(list_of_keys)

    @staticmethod
    def save_data_to_file(file_name, list_of_keys):
        objfile = open(file_name, "ab")
        pickle.dump(list_of_keys, objfile)
        objfile.close()

    @staticmethod
    def read_data_from_file(file_name):
        try:
            objfile = open(file_name, "rb")
            list_of_keys = pickle.load(objfile)
            objfile.close()
            return list_of_keys
        except FileNotFoundError as f:
            print("File does not exist yet.")
        except AttributeError:
            pass

class IO:
    @staticmethod
    def print_menu_Tasks():
        """
        Display a menu of choices to the user
        :return: nothing
         """
        print("""
        Menu of Options
        1) Add a new keyboard
        2) Save Keyboards to File
        3) Show current keyboard list
        4) Exit Program
        """)

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        return choice

    @staticmethod
    def asking_add_data():
        try:
            keyboard = input("What keyboard would like to add? ")
            price = int(input("How much does the keyboard cost? "))
        except ValueError as v:
            print("Built in Python Error Info")
            print()
            print(v, v.__doc__, type(v))
            print()
            print("**************************")
            print("My custom message:")
            print("Please only use numbers")
            print("***************************")
            print()
            print("Try again!")
            price = int(input("How much does the keyboard cost? (You only get one more chance ) "))
        except ValueError as v:
            print("Built in Python Error Info")
            print()
            print(v, v.__doc__, type(v))
            print()
            print("**************************")
            print("My custom message:")
            print("Please only use numbers")
            print("***************************")
            print("Goodbye")
        lstkeyboard = [keyboard, price]
        return lstkeyboard


# main body#
while (True):
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    print()  # adding a new line for looks

    if (strChoice.strip() == "1"): # add data
        keyboard, price = IO.asking_add_data()
        Processor.adding_data(keyboard, price, lstkeyboard)
        #IO.print_menu_Tasks()
    elif (strChoice.strip() == "2"): # save data
        print("Would you like to save the keyboard list? ")
        answers = input("Enter 'y' and 'n': ")
        try:
            if answers == 'y':
                Processor.save_data_to_file(strFileName, lstkeyboard)
                print("Saved!")
        except:
            print('Your data is not saved')

    elif (strChoice.strip() == "3"): # show current data
        print("Your current keyboard list is: ")
        print(Processor.read_data_from_file(strFileName))
        #IO.print_menu_Tasks()  # Shows menu

    elif(strChoice.strip() == "4"):
        print("Do you want to exit the program? ")
        answers = input("Please press enter/return key to exit")
        print("Goodbye")
        break

    # else:
    #     print("You have not provided a valid selection")

