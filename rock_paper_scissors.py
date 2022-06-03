from random import choice

def play():
    # global storage
    score_board = {}
    choices = ['rock', 'paper', 'scissors']
    break_flag = False

    # Step 1: Greet & ask for player name.
    print("\nWelcome to rock paper scissors!")
    name = input("\nwhat is your name?: ")
    # score_board[name]
    
    while True:

        if break_flag:
            break

        # Step 2: Choose to play
        start  = input("\nWould you like to play? (type 'yes' or 'no'): ")

        # Step 3a: Play Game
        if start.lower().strip() == 'yes':
            while True:
                
                # y=0
                # c=0

                # Step4: User chooses option
                user_input = input("\nChoose 'rock', 'paper', or 'scissors': ") 
                computer_input  = choice(choices)

                # Step5a: User Chooses Rock
                if user_input == 'rock' and computer_input == 'paper':
                    print(f"\nThe computer chose {computer_input}, you lose!")
                    # score_board[name] = {'you': y += 1, 'computer':  c}
                elif user_input == 'rock' and computer_input == 'scissors':
                    print(f"\nThe computer chose {computer_input}, you win!")
                elif user_input == 'rock' and computer_input == 'rock':
                    print(f"\nThe computer chose {computer_input}, it's a tie!")   #what happens when there's a 

                # Step 5b: User Chooses Paper    
                elif user_input == 'paper' and computer_input == 'paper':
                    print(f"\nThe computer chose {computer_input}, it's a tie!") #what happens when there's a tie
                elif user_input == 'paper' and computer_input == 'scissors':
                    print(f"\nThe computer chose {computer_input}, you lose!")
                elif user_input == 'paper' and computer_input == 'rock':
                    print(f"\nThe computer chose {computer_input}, you win!")  
                    
                # Step 5c: User Chooses scissors
                elif user_input == 'scissors' and computer_input == 'paper':
                    print(f"\nThe computer chose {computer_input}, you win!")
                elif user_input == 'scissors' and computer_input == 'scissors':
                    print(f"\nThe computer chose {computer_input}, its a tie!")    #what happens when there's a tie
                elif user_input == 'scissors' and computer_input == 'rock':
                    print(f"\nThe computer chose {computer_input}, you lose!")   
                
                # Step 5d: Leave game
                elif user_input == 'quit':
                    break_flag = True
                    break
                else:
                    print("\ninvalid input...")

        # Step 5d1: End game
        elif break_flag:
            print("\nThanks for playing!")
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
# counting score, return tally 
# extra feature: ie, name
 
# scoreboard = {}

