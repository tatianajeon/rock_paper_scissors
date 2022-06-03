from random import choice

def play():
    # global storage
    score_board = {}
    choices = ['rock', 'paper', 'scissors']
    break_flag = False

    # Step 1: Greet & ask for player name.
    print("\nWelcome to rock paper scissors!\n")
    name = input("\nwhat is your name?: ")
    score_board[name] = {}
    y=0
    c=0
    score_board[name]['you'] = y
    score_board[name]['computer'] = c


    while True:

    
        if break_flag:
            break

        # Step 2: Choose to play
        start  = input("\nWould you like to play? (type 'yes' or 'no'): ")

        # Step 3a: Play Game
        if start.lower().strip() == 'yes':
            while True:
                
                

                # Step4: User chooses option
                user_input = input("\nChoose 'rock', 'paper', or 'scissors': ") 
                computer_input  = choice(choices)

                # Step5a: User Chooses Rock
                if user_input == 'rock' and computer_input == 'paper':
                    print(f"\nThe computer chose {computer_input}, you lose!")
                    c += 1  
                    score_board[name]['computer'] = c
                    print(f"\n{score_board[name]}")
                    
                elif user_input == 'rock' and computer_input == 'scissors':
                    print(f"\nThe computer chose {computer_input}, you win!")
                    y += 1  
                    score_board[name]['you'] = y
                    print(f"\n{score_board[name]}")

                elif user_input == 'rock' and computer_input == 'rock':
                    print(f"\nThe computer chose {computer_input}, it's a tie!") 
                    print(f"\n{score_board[name]}")




                # Step 5b: User Chooses Paper    
                elif user_input == 'paper' and computer_input == 'paper':
                    print(f"\nThe computer chose {computer_input}, it's a tie!") 
                    print(f"\n{score_board[name]}")
                    
                elif user_input == 'paper' and computer_input == 'scissors':
                    print(f"\nThe computer chose {computer_input}, you lose!")
                    c += 1  
                    score_board[name]['computer'] = c
                    print(f"\n{score_board[name]}")

                elif user_input == 'paper' and computer_input == 'rock':
                    print(f"\nThe computer chose {computer_input}, you win!")  
                    y += 1  
                    score_board[name]['you'] = y 
                    print(f"\n{score_board[name]}")



                    
                # Step 5c: User Chooses scissors
                elif user_input == 'scissors' and computer_input == 'paper':
                    print(f"\nThe computer chose {computer_input}, you win!")
                    y += 1  
                    score_board[name]['you'] = y 
                    print(f"\n{score_board[name]}")

                elif user_input == 'scissors' and computer_input == 'scissors':
                    print(f"\nThe computer chose {computer_input}, its a tie!")    
                    print(f"\n{score_board[name]}")
                    
                elif user_input == 'scissors' and computer_input == 'rock':
                    print(f"\nThe computer chose {computer_input}, you lose!")
                    c += 1  
                    score_board[name]['computer'] = c
                    print(f"\n{score_board[name]}")
                



                # Step 5d: Leave game
                elif user_input == 'quit':
                    break_flag = True
                    print("\nThanks for playing!")
                    print(f"\n{score_board[name]}")
                    break

                elif user_input == 'new':
                    y=0
                    c=0
                    name = input("\nWhose playing now?: ")
                    score_board[name] = {}

                else:
                    print("\ninvalid input...")

        # Step 5d1: End game
        elif break_flag:
            
            break
        
        # Step 3b: Don't play
        elif start.lower().strip() == 'no':
            print("\nThanks for visiting!")
            break
        
        # 3c: Try again
        else:
            print("\nInvalid input...")

play()




# TO DO LIST
#
# extra feature: ie, name

 
# scoreboard = {}

