print("Welcome to the rollercoster!")
height = int(input("What is your height in cm?"))
if height >= 120: 
    print("you can ride the rollercoaster!")
    age = int(input("what is your age?"))
    if age < 12: 
        bill = 5
        print("Chlid tickest are $5.")
    elif age <=18: 
        bill = 7
        print("Youth tickets are $7.")
    elif age >=45 and age <55:
        print("Everythinf is ok. have a free ride on us!")
    else: 
        bill = 12
        print("Adult tickers are $12.")
    
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo =="Y":  
      bill+= 3
    
    print(f"your final bill is {bill}")
else: 
    print("sorry, You have to grow taller before you  can ride.")