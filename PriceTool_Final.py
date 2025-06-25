#add all the stuff for functions -- step 1
#-- This adds pretty decorations to stuff


def make_statement(statement, decoration):
    """ Emphasises headings by adding decoration
     at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"
#-- this is the instructions i will use the yes no to ask whether they want do display it
def instructions():
    print(make_statement("instructions", "⚙️"))

    print('''
First Enter Your Budget and then 
the code will show what the best option is and ask to buy it 
if you cant afford the item then the code will give you an ultimatum 
and ask if you would want to buy the next best thing
and if the user doesnt have enough for anything it kicks you out
Ps: The Weight Will Be Displayed In grams.

    ''')

#-- this is my number checker it checks for float numbers so not zero
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
#-- this is a yes no checker it checks whether the user say yes or no and nothing else
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

# add the variables hard coded in and the lists  -- step 2
#--  stores the list of stuff for the price tool to compare
#--  cost of the chips
chipsc  =5.00
#--  weight of the chips in kilos
chipswk =.50
#--  weight of the chips in grams
chipswg =500
#--  unit price of the chips
chipsup =10.00

#-- cost of the apple
applec = 1.00
#--  weight of the apple in kilos
applewk =.25
#--  weight of the apple in grams
applewg =250.00
#--  unit price of the apple per kilo
appleup =4.00
#-- cost of the chocolate
chocolatec =5.25
#-- weight of the chocolate in kilos
chocolatewk =7.50
#--  weight of the chocolate in grams
chocolatewg = 7500.00
#--  unit price of the chocolate per kilo
chocolateup =0.70
chip = [chipsc, chipswg,chipswk,chipsup]
apple = [applec,applewg,applewk,appleup]
choc = [chocolatec,chocolatewg,chocolatewk,chocolateup]
weight = [chipswg , applewg , chocolatewg]
cost = [chipsc,applec,chocolatec]
names = ['Chips','Apples','Chocolate']
unitprice = [chipsup, appleup , chocolateup]
#-- display name and ask for instructions -- step 3
print(make_statement("Price Tool", "🍴"))
#-- asks if the user would like to see the instructions
print()
want_instructions = yes_no_check("do you want to see the instructions")
print()

if want_instructions == "yes":
    instructions()
# add the questions for budget -- step 4
    #--Asks what the users budget is
budget = num_check("What is Your Budget")
#-- prints out the users budget in dollars in case you forgot
print(f" {budget:.2f}$ is your budget")
#present a spread for the price tool items -- step 5
#-- prints out the multiple different options and their category such as weight grams , weight kilos , cost $ , unit price $, User budget
if budget >= min(cost):
    from tabulate import tabulate
    a = [['Chips',f'{chipswg:.2f}g',f'{chipswk:.2f}Kg' ,f'{chipsc:.2f}$' ,f'{chipsup:.2f}$',f'{budget:.2f}$' ], ['Apple',f'{applewg:.2f}g',f'{applewk:.2f}Kg',f'{applec:.2f}$',f'{appleup:.2f}$' ], ['Chocolate',f'{chocolatewg:.2f}g',f'{chocolatewk:.2f}Kg',f'{chocolatec:.2f}$',f'{chocolateup:.2f}$' ]] # data
    b = ['Name', 'Weight Grams','Weight Kilos', 'Cost[$]', 'Unit Price per kilo','User Budget'] # headers
    print("this is the available products")
    print(tabulate(a, headers=b ,tablefmt="pipe"))
    # mark unaffordable stuff and adjust all accordingly if none affordable skip to step 9 -- step 6
    # Remove marked items and the others -- step 7
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

    # Checks for items in unit price that arent the minimum and makes them 100 including cost and weight
    for i in range(len(cost)):
        if unitprice[i] > min(unitprice):
            unitprice[i] = 100
            cost[i] = 100
            weight[i] = 100







    # Creating a copy of the list to avoid modifying it during iteration
    # removes items that are 100
    for x in cost[:]:
        if condition(x): # if it meets the condition of being zero remove it
            cost.remove(x)
            unitprice.remove(x)
            weight.remove(x)


    # tell what the best option is skip step 9   -- step 8
    ## https://www.datacamp.com/tutorial/python-tabulate used datacamp for ideas on how to display this
    # Import the tabulate module
    if cost == 1:
        name = "Apple"
    elif cost == 5:
        name = "Chips"
    else:
        name = "Chocolate"
    from tabulate import tabulate

    # Sample data: list of lists
    data = [
        [name,f"{cost[0]:.2f}$",f"{weight[0]:.2f}g",f"{unitprice[0]:.2f}$"]

    ]
    remain = budget - cost[0]
    # Creating a table with headers and a grid format
    table = tabulate(
        data,
        headers=["Name", "Cost", "Weight","UnitPrice(Per Kilo)"],
        tablefmt="pipe"
    )

    print(table)
    buy = yes_no_check(f"would you like to buy {name} for {cost[0]:.2f}$  "
                       f"You Have {budget:.2f}$  ")
    if buy == "yes":
        print(f"you have bought {name} for {cost[0]:.2f}$ and have"
              f" S{remain:.2f}$ left ")
    # say your poor -- step 9
else:
    print("you cant afford anything comeback with more money")