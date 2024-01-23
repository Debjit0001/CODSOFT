import os

def calculator():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n\t~~:Calculator:~~\n')

        # Getting input from the user for the first number
        num1 = input("Enter first number: ")
        try:
            num1 = float(num1)
        except ValueError:
            print('\nPlease enter a valid number')
            input('Press enter to continue...')
            continue

        print('\nChoose from: (+, -, *, /, %)')
        operator = input("Enter operator: ")

        # Performing the calculation based on the operator
        if operator in ('+', '-', '*', '/', '%'):
            num2 = input("\nEnter second number: ")
            try:
                num2 = float(num2)
            except ValueError:
                print('\nPlease enter a valid number!')
                input('Press enter to continue...')
                continue

            print('---------------------------')

            # Checking for division by zero
            if num2 == 0 and operator == '/':
                print("Cannot divide by zero!")
                input('Press enter to continue...')
                continue
            
            print(f'Result = {eval(str(num1) + operator + str(num2))}')
        else:
            print("\nInvalid operator")
            input('Press enter to continue...')
            continue

        # Asking if the user wants to continue
        choice = input("\nDo you want to perform another calculation? (y/n): ")
        if choice.lower() != "y":
            print('Exiting the program. Goodbye! \n')
            break

if __name__ == "__main__":
    calculator()
