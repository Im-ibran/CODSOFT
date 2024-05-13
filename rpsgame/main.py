import random

options = ("rock", "paper", "scissors")

print("     RPS human vs machine ")

#these are the variables that are set to 0 at start
human_points = 0
machine_points = 0
num_rounds = 0

#this loop continues untill user enters y after playing a round
while True:
    you = None
    machine = random.choice(options)

#This loop continues to run as long as the user's choice (you) is not found within the options
    while you not in options:
        you = input("Enter a choice (rock, paper, scissors):  ")

#this will just print what both choosed
    print(f"\nYOU: {you}")
    print(f"MACHINE: {machine}")

#Below is RPS logic plus it will also update score based on who wins
    if you == machine:
        print(" It's a draw! ")

    elif (you == "rock" and machine == "scissors"):
        print("You win")
        human_points += 1
    elif(machine == "rock" and you == "scissors"):
        print("Machine wins")
        machine_points += 1
    elif (you == "scissors" and machine == "paper"):
        print(" You win! ")
        human_points += 1
    elif (you == "scissors" and machine == "paper"):
         print("Machine wins")
         machine_points += 1
    elif (you == "paper" and machine == "rock"):
         print(" You win! ")
         human_points += 1
    elif(you == "paper" and machine == "rock"):
         print("Machine wins")
         machine_points += 1
    else:
        print(" Machine wins! ")
        machine_points += 1


#after a match no of round will be Updated here
    num_rounds += 1

# this will show current score and number of rounds
    print(f"\nYour score: {human_points}")
    print(f"Machine's score: {machine_points}")
    print(f"Number of rounds played: {num_rounds} \n")

#loops will break if user enters anyhing other than y otherwise goes for another round
    if not input("Want to Play another round? (y/n): ") == "y":
        break
    print(" [ Thanks for playing ] ")