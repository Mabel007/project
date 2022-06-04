import random


# welcome page
print("Welcome to Rock Paper scissors \n")

# user input
myChoice = input("What is your input?\n Enter R, P, S  \n").upper().strip()
# computer selection
computerChoice = ['R', 'P', 'S']
computer = random.choice(computerChoice)
#print(f'computer picked{computer}')

while True:
    if myChoice == computer:
        print("it's a tie")
    elif myChoice == "R":
        if computer == "S":
            print(
                f'you picked(myChoice) for Rock and computer picked {computer} for scissor')
            print("You Win")
        else:
            print("You lose, computer Wins!")
    elif myChoice == "P":
        if computer == "R":
            print(
                f'you picked(myChoice) for Paper and computer picked {computer} for Rock')
            print("You Win")
        else:
            print("You lose, computer Wins!")
    elif myChoice == "S":
        if computer == "P":
            print(
                f'you picked(myChoice) for Scissor and computer picked {computer} for Paper')
            print("You Win")
        else:
            print("You lose, computer Wins!")
    else:
        print('Enter a valid input')

        # if user wants to restart the game
    print('Do you want to restart the game?')
    answer = input('Yes or No \n').upper()

    if answer != 'Yes':
        break
    else:
        continue
