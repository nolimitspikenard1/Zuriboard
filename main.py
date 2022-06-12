import random2
while True:
    game = ["rock", "paper", "scissors"]
    CPU = random2.choice(game)
    player = None
    while player not in game:
        player = input("rock, paper, or scissors: ").lower()
    if player == CPU:
        print("player: ",player)
        print("CPU: ",CPU)
        print("Tie")  
    elif player == "rock":
        if CPU == "scissors":
            print("player: ",player)
            print("CPU: ",CPU)
            print("You Win!")       
        if CPU == "paper":
            print("player: ",player)
            print("CPU: ",CPU)
            print("You Lose!")
    elif player == "scissors":
        if CPU == "paper":
            print("player: ",player)
            print("CPU: ",CPU)
            print("You Win!")
        if CPU == "rock":
            print("player: ",player)
            print("CPU: ",CPU)
            print("You Lose!")   
    elif player == "paper":
        if CPU == "rock":
            print("player: ",player)
            print("CPU: ",CPU)
            print("You Win!")
        if CPU == "scissors":
            print("player: ",player)
            print("CPU: ",CPU)
            print("You Lose!")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye!")          

         
        







   