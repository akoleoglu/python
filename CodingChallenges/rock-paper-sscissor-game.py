
import random;

game_options = ["scissors","paper","rock"]

def game():
    user_wins = 0
    comp_wins = 0
    while (True):
        user_input = input("Please enter your weapon :")
        lower_case = user_input.lower()
        computer_input = random.choice(game_options)
        print("Computer picked ", computer_input)
        if ((lower_case != "scissors") and (lower_case != "rock") and (lower_case != "paper")):
            print("Please enter your weapon correctly!!! Try again ")
        else:
            if computer_input == lower_case:
                print("tie - no one wins")
                pass
            elif computer_input == "scissors" and lower_case == "paper":
                print("scissors beats paper - computer wins")
                comp_wins+=1
                if comp_wins==3:
                    print(f"User won {user_wins} time(s) and computer won {comp_wins} time(s)")
                    print("Computer has won the game!")
                    return False
               
            elif computer_input == "scissors" and lower_case == "rock":
                print("rock beats scissors - user wins")
                user_wins+=1
                if user_wins==3:
                    print(f"User won {user_wins} time(s) and computer won {comp_wins} time(s)")
                    print("User has won the game!")
                    return False
                      
            elif computer_input == "rock" and lower_case == "scissors":
                print("rock beats scissors - computer wins")
                comp_wins+=1
                if comp_wins==3:
                    print(f"User won {user_wins} time(s) and computer won {comp_wins} time(s)")
                    print("Computer has won the game!")
                    return False
            elif computer_input == "rock" and lower_case == "paper":
                print("paper beats rock - user wins")
                user_wins+=1
                if user_wins==3:
                    print(f"User won {user_wins} time(s) and computer won {comp_wins} time(s)")
                    print("User has won the game!")
                    return False
                      
            elif computer_input == "paper" and lower_case == "rock":
                print("paper beats rock - user wins")
                comp_wins+=1
                if user_wins==3:
                    print(f"User won {user_wins} time(s) and computer won {comp_wins} time(s)")
                    print("User has won the game!")
                    return False
            elif computer_input == "paper" and lower_case == "scissors":
                print("scissors beats paper - user wins")
                user_wins+=1
                if user_wins==3:
                    print(f"User won {user_wins} time(s) and computer won {comp_wins} time(s)")
                    print("User has won the game!")
                    return False
                
game()









