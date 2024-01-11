import random

options = ["rock", "paper", "scissors"]
myscore = 0
computerscore = 0

print("*************************")
print("ROCK PAPER SCISSORS GAME!")
print("*************************")

option = input("\nEnter one of the following options (Rock, Paper, Scissors, or Quit):")
option = option.lower()

while option != "quit":
    if option in options:      
        random_option = random.choice(options)
        print("You picked: " + option)
        print("Computer picked: " + random_option)
        if option == random_option:
            print("Tie!!!")
        elif option == "scissors" and random_option == "paper":
            print("You Win!!!")
            myscore = myscore + 1
        elif option == "paper" and random_option == "rock":
            print("You Win!!!")
            myscore = myscore + 1
        elif option == "rock" and random_option == "scissors":
            print("You Win!!!")
            myscore = myscore + 1
        else:
            print("Computer Wins!!!")
            computerscore = computerscore + 1
    else: 
        print("Incorrect Option")

    print("Your Score: "+ str(myscore), "Computer Score: " + str(computerscore))
    option = input("\nEnter one of the following options (Rock, Paper, Scissors, or Quit):")
    option = option.lower()

print("Bye Bye!")