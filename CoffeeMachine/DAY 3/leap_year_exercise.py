year = int(input("which year do want to check"))

# if year% 4 ==0 and (year% 100 != 0 or year % 400==0) : print("This is a leap year.")

# else :print("This is not a leap year")

if year% 4 ==0:
    if year% 100 ==0:
       if year% 400 == 0:
          print("Leap year")
       else:print("Not a leap year")

    else:
        print("Leap year")
else:
    print("Not a leap year")
