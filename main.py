import random
import os
import re
import time
os.system('cls')

print("***TYPE THE FIRST LETTER OF YOUR CHOICE\n")
user=0
ai=0
tie=0
match=0

while (1):
    print("\n")
    print("\t\tTOTAL MATCH - " + str(match)+"\n")
    print("User:\t" + str(user) + "\n")
    print("AI  :\t" + str(ai) + "\n")
    print("Tie :\t" + str(tie) + "\n")
    match+=1
    print ("\nRock, Paper or Scissors? Do you DARE?")
    print ("Say NO to stop")
    my_choice = input("What Are You? Rock, Paper, or Scissors: ")

    if re.match("[No,NO,no,nO]",my_choice):
        print("\n\nSO....You Don't Want to Play...Huh!")
        if user>ai:
            print("You are the winner!  :(")
        elif ai>user:
            print("I am the WINNER! Don't be Sad. :)")
        elif match==1:
            print("Hey! YOU DIDN'T EVEN PLAY THE GAME....You're BORING  :(")
        else:
            print("We tied the Game!    :|")
        time.sleep(7)
        break

    if not re.match("[sSrRpP]", my_choice):
        print ("Wrong Input !!!! Choose the RIGHT One")
        match-=1
        continue

    print ("You chose - " + my_choice)
    option = ['P', 'S', 'R']
    ai_choice = random.choice(option)
    print ("I chose -  " + ai_choice)

    if ai_choice == str.upper(my_choice):
        print ("Tie !!! ")
        tie+=1
        
    elif ai_choice == 'S' and my_choice.upper() == 'P':      
        print ("Scissors beats paper.......I win!     :)")
        ai+=1
        continue

    elif ai_choice == 'P' and my_choice.upper() == 'R':      
        print ("Paper beat rock............I win!     :)")
        ai+=1
        continue

    elif ai_choice == 'R' and my_choice.upper() == 'S':      
        print ("Rock beats Scissors........I win!     :) ")
        ai+=1
        continue

    else:       
        print ("You win!   :(")
        user+=1