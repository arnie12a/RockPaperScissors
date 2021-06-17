import random

def UserWins():
	print("Congrats! You won beat the computer")

def ComputerWins():
	print("You lost to the computer. You will get them next time!")
	
def Tie():
	print("You tied with the computer")

numWins = 0
numLosses = 0
numTies = 0

while True:
	print("\nRock, Paper, Scissors, Shoot!")
	guessWord = str(input())
	if guessWord == "q":
		print("User Wins: " + str(numWins))
		print("Computer Wins " + str(numLosses))
		if(numWins > numLosses):
			print("CONGRATS YOU ARE THE ALLTIME WINNER")
		elif(numLosses > numWins):
			print("YOU SUCK")
		else:
			print("THERE IS AN ALLTIME TIE BETWEEN YOU AND THE COMPUTER")
		break
	guessWord = guessWord.upper()
	if guessWord == "R":
		guessWord = "ROCK"
	elif guessWord == "S":
		guessWord = "SCISSORS"
	elif guessWord == "P":
		guessWord = "PAPER"
	else:
		pass
	print("You chose " + guessWord)
	possibilities = ["ROCK", "PAPER", "SCISSORS"]
	computerGuess = random.choice(possibilities)
	print("The computer chose " + computerGuess)
	if guessWord in possibilities:
		if guessWord == "ROCK" and computerGuess == "PAPER":
			ComputerWins()
			numLosses = numLosses + 1
			print("User Wins: " + str(numWins))
			print("Computer Wins " + str(numLosses))
		elif guessWord == "ROCK" and computerGuess == "SCISSORS":
			UserWins()
			numWins = numWins + 1
			print("User Wins: " + str(numWins))
			print("Computer Wins " + str(numLosses))
		elif guessWord == "PAPER" and computerGuess == "ROCK":
			UserWins()
			numWins = numWins + 1
			print("User Wins: " + str(numWins))
			print("Computer Wins " + str(numLosses))
		elif guessWord == "PAPER" and computerGuess == "SCISSORS":
			ComputerWins()
			numLosses = numLosses + 1
			print("User Wins: " + str(numWins))
			print("Computer Wins " + str(numLosses))
		elif guessWord == "SCISSORS" and computerGuess == "PAPER":
			UserWins()
			numWins = numWins + 1
			print("User Wins: " + str(numWins))
			print("Computer Wins " + str(numLosses))
		elif guessWord == "SCISSORS" and computerGuess == "ROCK":
			ComputerWins()
			numLosses = numLosses + 1
			print("User Wins: " + str(numWins))
			print("Computer Wins " + str(numLosses))
		else:
			Tie()
			numTies = numTies + 1
			print("Number of ties: " + str(numTies))
	else:
		print("Invalid input")
