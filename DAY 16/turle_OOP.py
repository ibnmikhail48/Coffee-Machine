# from turtle import Turtle, Screen
# ## attributes are the thing that an object i.e data that it holds
# ## method are functions that associated with that object i,e things that it does 

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
# my_screen = Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water","Fire"])
table.align = "l"
print(table)