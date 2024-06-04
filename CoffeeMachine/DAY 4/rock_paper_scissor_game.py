rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player_input=int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))



if player_input ==0:print(rock)
elif player_input==1:print(paper)
else :print(scissors)

import random

random_play = random.randint(0,2)

print(f"Computer chose:")

if random_play == 0: 
    print(rock) 
elif random_play==1:
    print(paper)
elif random_play==2:
    print(scissors)


if (player_input==0)and(random_play==0):print("Draw")
elif (player_input==0)and(random_play==1):print("You Lose")
elif (player_input==0)and(random_play==2):print("You Win")

if (player_input==1)and(random_play==1):print("Draw")
elif (player_input==1)and(random_play==2):print("You Lose")
elif (player_input==1)and(random_play==0):print("You Win")

if (player_input==2)and(random_play==2):print("Draw")
elif (player_input==2)and(random_play==0):print("You Lose")
elif (player_input==2)and(random_play==1):print("You Win")












