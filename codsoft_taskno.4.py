import random, os, time

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(user_choice_val, computer_choice):
    choices = ["Rock", "Paper", "Scissors"]
    user_choice = choices[user_choice_val-1]
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "YOU WIN!!"
    else:
        return "Computer wins!"
    
def interface(user_score, computer_score):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n~~:Rock Paper Scissors Game:~~\n')
    
    print(f"Score - You: {user_score}, Computer: {computer_score}")

def main():
    user_score = 0
    computer_score = 0

    while True:
        interface(user_score, computer_score)
        
        print('\nChoose from: \n1. Rock \n2. Paper \n3. Scissors')
        user_choice = int(input('enter your choice: '))
        if not 1 <= user_choice <= 3:
            input('\nInvalid choice! Press enter to continue..')
            continue
        
        computer_choice = get_computer_choice()
        
        os.system('cls' if os.name == 'nt' else 'clear')
        interface(user_score, computer_score)
        
        print('\nRock..', end=" ")
        time.sleep(.5)
        print('Paper..', end=" ")
        time.sleep(.6)
        print('Scissors.. \n',)

        result = determine_winner(user_choice, computer_choice)
        print('\n' + result)

        if "YOU WIN!!" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("\nThanks for playing! Goodbye..\n")
            break

if __name__ == "__main__":
    main()
