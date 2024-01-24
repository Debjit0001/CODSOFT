import random, string, os

def generate_password(length=8, complexity=1):
    password = ''
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length):
        ch = random.choice(characters)
        password += ch

    return password
    

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print('\n~~:Password Generator:~~\n')

        try:
            length = int(input('Please specify the length of the password: '))

            print('\nPlease specify the complexity of the password. \n1. weak (contains only letters) \n2. moderate (contains letters and numbers \n3. strong (contains letters, numbers and punctuations))')
            complexity = int(input('enter your choice: (1/2/3): '))

            if not 1 <= complexity <= 3:
                print('\nInvalid input! Please enter 1, 2, or 3 for complexity.')
            else:
                password = generate_password(length, complexity)
                print('\nGenerated password:', password)

            choice = input('\nDo you want to generate the password again? (y/n): ')
            if choice.lower() != 'y':
                print('\nExiting the program. Goodbye! \n')
                break
        except ValueError:
            print('\nInvalid input! Please enter a valid number.')

if __name__ == '__main__':
    main()
