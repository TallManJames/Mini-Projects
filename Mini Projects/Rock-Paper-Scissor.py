import random

print("Before we begin, what is your name?")
playerName = input()

print("Next, what score do you want this game to go to?")
winningScore = int(input())

print(f"Perfect! Just a heads-up, the game is first to {winningScore}. Good luck {playerName}!")

playerScore = 0
computerScore = 0

while playerScore < winningScore and computerScore < winningScore:
    choices = ['rock','paper','scissors']

    computerChoice = random.choice(choices)

    print("\nOk, it is time for you pick:\nRock\nPaper\nor Scissors\n")
    givenChoice = input().lower()
    print("")   #this is to make space

    if givenChoice not in choices:
        print("Error, check spelling and try again")
    if givenChoice == computerChoice:
        print("It's a draw!")
    if givenChoice == 'rock' and computerChoice == 'scissors':
        print("You Win")
        playerScore += 1
    if givenChoice == 'scissors' and computerChoice == 'paper':
        print("You Win")
        playerScore += 1
    if givenChoice == 'paper' and computerChoice == 'rock':
        print("You Win")
        playerScore += 1
    if givenChoice == 'rock' and computerChoice == 'paper':
        print("You Lose")
        computerScore += 1
    if givenChoice == 'scissors' and computerChoice == 'rock':
        print("You Lose")
        computerScore += 1
    if givenChoice == 'paper' and computerChoice == 'scissors':
        print("You Lose")
        computerScore += 1

    print(f"Your score: {playerScore}\nComputer's score: {computerScore}")

if playerScore == winningScore:
    print(f"\nCongratulations {playerName}, you win!")

if computerScore == winningScore:
    print(f"\nSorry {playerName}, you lose this time. Play again soon!")
