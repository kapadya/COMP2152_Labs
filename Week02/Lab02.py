import random

choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Choose one of the following numbers: 1-Rock | 2-Paper | 3-Scissors: ")

if not playerChoice.isdigit():
    print("Error! Please enter a valid number.")
    exit()

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error! Please choose a number between 1 and 3.")
    exit()
   
computerChoice = random.randint(1, 3)

playerMove = choices[playerChoice - 1]
computerMove = choices[computerChoice - 1]

print ("Your choice:", playerChoice, "-", playerMove, "| Computer's choice:", computerChoice, "-", computerMove)

if playerChoice == computerChoice:
    print("It's a tie!")
elif (playerChoice - computerChoice) % 3 == 1:
    print("You Win!", playerMove, "beats", computerMove)
else:
    print("You Lose!", computerMove, "beats", playerMove)