# states_or_america = ["delware" , "new york" , "batman"]
# #append funxtion is use to add items to a list
# states_or_america.append("victorland")

# #to change items on a list 
# states_or_america[1]="ceware"
# print(states_or_america)  

name_string = input ("Give me everybody's names, seperated by a comma.\n").lower()
name = name_string.split(",")

import random

# name_items=len(name)#to get the total number of items in a list

# random_name = random.randint(0, name_items - 1)
# who_will_pay = name[random_name]
who_will_pay = random.choice(name)
print(who_will_pay+ " is going to buy the meal today")

