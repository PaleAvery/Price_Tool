#add all the stuff for functions -- step 1
#-- This adds pretty decorations to stuff

# this allows me to make my instructions variable to look cool
def make_statement(statement, decoration):
    """ Emphasises headings by adding decoration
     at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"
def int_check(question):
    """Checks users enter an integer that is more than zero (or the 'xxx' exit code)"""

    error = "oops - please enter an integer."

    while True:

        try:

            response = int(input(question))


            return response
        except ValueError:
            print(error)
#-- this is the instructions I will use the yes no to ask whether they want to do display it
def instructions():
    print(make_statement("instructions", "⚙️"))

    print('''
Welcome to The Price Tool
This code will compare prices of which you can afford and
Then Decide the best Item for your budget 
So First Put in Your Budget 
then it will display the whole list of items 
and then show the Best thing you can Afford 
Then You can pick Whether you would like
To Buy It

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
#-- this is a yes no checker it checks whether the user say yes or no and rejects anything else
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
# im using the yes no checker in order to see if the user wants to read the instructions if not it won't display
if want_instructions == "yes":
    instructions()
# add the questions for budget -- step 4
    #--Asks what the users budget is
budget = num_check("What is Your Budget")
# if name is exit code break out of loop

#-- prints out the users budget in dollars ($)
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

    # Checks for items in unit price that aren't the minimum and makes them 100 including cost and weight
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
    if cost[0] == 1:
        name = "Apple"
    elif cost[0] == 5:
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
    print("This is the best priced item i could find.")
    table = tabulate(
        data,
        headers=["Name", "Cost", "Weight","UnitPrice(Per Kilo)"],
        tablefmt="pipe"
    )

    print(table)
    buy = yes_no_check(f"would you like to buy {name} for {cost[0]:.2f}$  "
                       f"You Have {budget:.2f}$  ")
    # if you say yes you will buy the thing and subtract the cost from your budget
    if buy == "yes":
        print(f"you have bought {name} for {cost[0]:.2f}$ and have"
              f" {remain:.2f}$ left ")
    else:
        if budget >= 5:
            option = yes_no_check(" Would you like to pick something else ")
            if option == "yes":
                from tabulate import tabulate

                a = [['Chips', f'{chipswg:.2f}g', f'{chipswk:.2f}Kg', f'{chipsc:.2f}$', f'{chipsup:.2f}$',
                      f'{budget:.2f}$'],
                     ['Apple', f'{applewg:.2f}g', f'{applewk:.2f}Kg', f'{applec:.2f}$', f'{appleup:.2f}$'],
                     ['Chocolate', f'{chocolatewg:.2f}g', f'{chocolatewk:.2f}Kg', f'{chocolatec:.2f}$',
                      f'{chocolateup:.2f}$']]  # data
                b = ['Name', 'Weight Grams', 'Weight Kilos', 'Cost[$]', 'Unit Price per kilo', 'User Budget']  # headers
                print("this is the available products pick one From 1-3 ")
                print(tabulate(a, headers=b, tablefmt="pipe"))
            # im using a while true statement in order to loop my code until they pick from 1 to 3
            while True:
                # im using an int check to make the user type 1 -3 for options and using an else statement to loop the code
                pick = int_check("pick something from 1 -3 ")
                # this displays the chips graph and says you bought it
                if pick == 1 and budget >= chipsc:
                    data = [
                        ["Chips", f"{chipsc:.2f}$", f"{chipswg:.2f}g", f"{chipsup:.2f}$"]

                    ]
                    remain = budget - cost[0]
                    # Creating a table with headers and a grid format
                    print("this is your item.")
                    table = tabulate(
                        data,
                        headers=["Name", "Cost", "Weight", "UnitPrice(Per Kilo)"],
                        tablefmt="pipe"
                    )
                    # this displays the table for the chips
                    print(table)
                    # this prints out that you bought the apple and shows how much money you have left
                    print(f"you have bought the Chips for {chipsc:.2f}$ and now have {budget - chipsc :.2f}$ left")
                    break
                    # this is what shows after the user presses option three  and displays the apple you bought
                elif pick == 2 and budget >= applec:
                    data = [
                        ["Chips", f"{applec:.2f}$", f"{applewg:.2f}g", f"{appleup:.2f}$"]

                    ]
                    remain = budget - cost[0]
                    # Creating a table with headers and a grid format
                    print("this is your item.")
                    table = tabulate(
                        data,
                        headers=["Name", "Cost", "Weight", "UnitPrice(Per Kilo)"],
                        tablefmt="pipe"
                    )
                    # this displays the table for the apple
                    print(table)
                    # this prints what you bought and how much money you have left
                    print(f"you have bought the Apple for {applec:.2f}$ and now have {budget - applec :.2f}$ left")
                    break
                # this is what shows when you press option three it displays the graph for chocolate and then says It's what you bought
                elif pick == 3 and budget >= chocolatec:
                    data = [
                        ["Chips", f"{chocolatec:.2f}$", f"{chocolatewg:.2f}g", f"{chocolateup:.2f}$"]

                    ]
                    remain = budget - cost[0]
                    # Creating a table with headers and a grid format
                    print("this is your item ")
                    table = tabulate(
                        data,
                        headers=["Name", "Cost", "Weight", "UnitPrice(Per Kilo)"],
                        tablefmt="pipe"
                    )
                    # this displays the table that was created
                    print(table)
                    # this prints what you bought and how much money you have left
                    print(f"you have bought the Chocolate for {chocolatec:.2f}$ and now have {budget - chocolatec :.2f}$ left")
                    break
                elif pick == "xxx":
                    print("you have quit")
                    break
                else:
                    print("You either didn't pick something between 1 and 3 "
                          "or you can't afford it try again  ")
                 



    # say you're poor -- step 9
else:
    print("you cant afford anything  come back with more money")