import os

def calculator():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n\t~~:Calculator:~~\n')
        # getting input from the user
        num1 = input("Enter first number: ")
        if not isinstance(float(num1), (int, float)):
            print('\nPlease enter a valid number')
            input('Press enter to continue...')
            continue

        print('\nChoose from: (+, -, *, /, %)')
        operator = input("enter operator: ")

        num2 = input("\nEnter second number: ")
        
        # checking for possible errors
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        if not isinstance(float(num2), (int, float)):
            print('\nPlease enter a valid number!')
            input('Press enter to continue...')
            continue
        
        print('---------------------------')
        
        # performing the calculation based on the operator
        if operator in ('+', '-', '*', '/', '%'):
            print(f'Result = {eval(num1 + operator + num2)}')
        else:
            print("Invalid operator")
            continue

        # asking if the user wants to continue
        choice = input("\nDo you want to perform another calculation? (y/n): ")
        if choice.lower() != "y":
            print('Exiting the program. Goodbye! \n')
            break

if __name__ == "__main__":
    calculator()
