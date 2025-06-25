# functions go herre

# adds cool decoration to headings
def make_statement(statement, decoration):
    """ Emphasises headings by adding decoration
     at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"
def instructions():
    print(make_statement("instructions", "⚙️"))

    print('''
First Enter Your Budget and then 
the code will show what the best option is and ask to buy it 
if you cant afford the item then the code will give you an ultimatum 
and ask if you would want to buy the next best thing
and if the user doesnt have enough for anything it kicks you out

    ''')
# checker for float numbers
def num_check(question, num_type="float"):
    """checks that response is a float or integer more than zero"""

    if num_type == "float":
        error = "please enter a number more than zero."
    else:
        error = "please enter an integer more than zero."

    while True:
        try:

            if num_type == "float":
                response = float(input(question))
            else:
                response = int(input(question))

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)
def yes_no_check(question):
    """Checks that users enter yes / y or no/n to a question"""
    #

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        if response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes(y) or no(n).\n")

# stores the list of stuff for the price tool to compare
# cost of the chips
chipsc  =5.00
# weight of the chips in kilos
chipswk =.50
# weight of the chips in grams
chipswg =500
# unit price of the chips
chipsup =10.00

#cost of the apple
applec = 1.00
# weight of the apple in kilos
applewk =.25
# weight of the apple in grams
applewg =250.00
# unit price of the apple per kilo
appleup =4.00

#cost of the chocolate
chocolatec =5.25
# weight of the chocolate in kilos
chocolatewk =7.50
# weight of the chocolate in grams
chocolatewg = 7500.00
# unit price of the chocolate per kilo
chocolateup =0.70




print(make_statement("Price Tool", "🍴"))
# asks if the user would like to see the instructions

    #Asks what the users budget is
budget = num_check("What is Your Budget")
# prints out the users budget in case you forgot IDK
print(f" {budget:.2f}$ is your budget")
# prints out the multiple different options and their category such as weight grams , weight kilos , cost $ , unit price $, User budget

# filters the remaining stuff in regard to budget in two-step
# step one check if user can afford stuff off of the general cost
chip = [chipsc, chipswg,chipswk,chipsup]
apple = [applec,applewg,applewk,appleup]
choc = [chocolatec,chocolatewg,chocolatewk,chocolateup]
weight = [chipswg , applewg , chocolatewg]
cost = [chipsc,applec,chocolatec]
names = ['Chips','Apples','Chocolate']
unitprice = [chipsup, appleup , chocolateup]

# makes items in the list equal zero when they're below the budget this is, so I can remove them from
# being used in the second step
# changes all things over budget to 100
for i in range(len(cost)):
    if cost[i] > budget:
        cost[i] = 100
        unitprice[i] = 100
        weight[i] = 100
condition = lambda o: o == 100  # condition cant be zero

# Creating a copy of the list to avoid modifying it during iteration
# removes items that are 100
for x in cost[:]:
    if condition(x): # if it meets the condition of being zero remove it
        cost.remove(x)
        unitprice.remove(x)
        weight.remove(x)
print(unitprice)
print(unitprice)
# Checks for items in unit price that arent the minimum and makes them 100 including cost and weight
for i in range(len(cost)):
    if unitprice[i] > min(unitprice):
        unitprice[i] = 100
        cost[i] = 100
        weight[i] = 100





print(unitprice)

# Creating a copy of the list to avoid modifying it during iteration
# removes items that are 100
for x in cost[:]:
    if condition(x): # if it meets the condition of being zero remove it
        cost.remove(x)
        unitprice.remove(x)
        weight.remove(x)
print(unitprice)
print(cost)
print(weight)
# filtering code source makes new list
# https://www.geeksforgeeks.org/python/remove-elements-from-a-list-based-on-condition-in-python/
# prints the current values i am using this to test
# finish step 1 and start step two by removing unalienable from list
# and now removing unit prices that cant be afforded














