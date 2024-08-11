import random
print("Rock beats Scissors!\nScissors beats Paper!\nPaper beats Rock!\n")
rock=''' rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper=""" paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors=""" scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
#print(rock)
game_images=[rock,paper,scissors]
choice=int(input("What do you choose?Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(game_images[choice])
#input string a cilo but computer er gen. int so , compare korte hole dutu same type hote hobe hence making in int
choice_comp=random.randint(0,2)
print("computer choose")
print(game_images[choice_comp])
if choice>=3 or choice<0:
    print("invalid no. you lose!")
elif(choice==0 and choice_comp==1):
    print("you lost !")
elif (choice == 0 and choice_comp == 2):
    print("you won !")
elif (choice == 1 and choice_comp == 2):
    print("you lost !")
elif (choice ==1 and choice_comp == 0):
    print("you won !")
elif (choice == 2 and choice_comp == 1):
    print("you won !")
elif (choice == 2 and choice_comp == 0):
    print("you lost !")
else:
    print("draw")