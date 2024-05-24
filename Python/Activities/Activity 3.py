
user1=input("Please enter Player 1 name:")
user2=input("Please enter Player 2 name:")

user1Answer=input(user1+ ": Please enter your choice-Rock,Scissor or Paper?").lower()
user2Answer=input(user2+ ": Please enter your choice-Rock,Scissor or Paper?").lower()


if user1Answer == user2Answer:
    print("It's a tie!")
elif user1Answer == 'rock':
    if user2Answer == 'scissors':
            print("Rock wins!")
    else:
            print("Paper wins!")

elif user1Answer == 'scissors':
    if user2Answer == 'paper':
            print("Scissors win!")
    else:
            print("Rock wins!")
elif user1Answer == 'paper':
    if user2Answer == 'rock':
            print("Paper wins!")
    else:
            print("Scissors win!")
else:
        print("Invalid input! You have not entered rock, paper or scissors, try again.")



