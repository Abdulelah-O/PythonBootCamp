import random


while True:
    PlayerChoice= input('Enter a choice [Rock , Papper , Scissors] :')
    RandomChoice = ['Rock' , 'Papper' , 'Scissors']
    RandomResult = random.choice(RandomChoice) #RandomChoice result from a a list
    print('Your Choice' , PlayerChoice , '\nRandomResult' , RandomResult )
    if PlayerChoice == RandomResult : 
      print('Its a tie')
    elif PlayerChoice == 'Rock' :
      if RandomResult == 'Papper' :
        print('Papper covers Rock!')

      else  :
        print('rock smash scissors!')
    elif PlayerChoice == 'Papper' :
      if RandomResult == 'Rock' :
            print('Paper covers rock!')
      else :
             print('Scissors cuts Papper!')
    elif PlayerChoice == 'Scissors' :
         if RandomResult == 'Papper' :
            print('Scissors cuts Papper! ')
         else :
            print('Rock smash scissors!')
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break


         



