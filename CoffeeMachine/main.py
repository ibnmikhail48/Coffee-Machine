# TODO: 2. Check that resources are sufficient to make drink order.
Menu= {
     "espresso": {
         "ingredients": {
             "water":50,
             "coffee": 18,
         },
     "cost":1.5,    }
     },
"latte": {
 "ingredients": {
"water": 200,
"milk": 150,
"coffee": 24, }
   },
     "cost":2.5,
        },
 "cappuccino": {
 "ingredients": {
     "water": 250,
     "milk": 100,
     "coffee": 24, }
 },
 "cost":3.0,
 },
 }
 resources = {
     "water": 300,
     "milk": 200,
     "coffee": 100,
 }


 While True:
    choice = input ("what would you like ? (espresso/latte/cappuccino): ")
 # TODO: 1 Print report of all coffee machine resources
