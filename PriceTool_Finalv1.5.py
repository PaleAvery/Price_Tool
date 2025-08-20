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

def weight_type(question):
    """Checks that users enter yes / y or no/n to a question"""
    #

    while True:
        response = input(question).lower()

        if response == "kilo" or response == "k":
            return 1
        if response == "grams" or response == "g":
            return 1/1000
        if response == "litres" or response == "l":
            return 1
        if response == "eggs" or response == "e" or response == "egg":
            return 56/1000
        if response == "tons" or response == "t" :
            return 1000
        if response == "millilitres" or response == "ml":
            return 1/1000

        else:
            print("please enter yes(y) or no(n).\n")

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
def not_blank(question):
    """Checks that a user response is not blank """

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this cant be blank. Please try again.\n")
# lists to hold ticket details
all_names = []
all_product_costs = []
all_product_weight  = []
all_product_weight_type = []
all_unitprice = []
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
productnum = 0
#-- prints out the users budget in dollars ($)
print(f" {budget:.2f}$ is your budget")

productmax = int_check("how many products do you want to add")
while productnum < productmax:
    name=not_blank("what is your products name ")
    all_product_weight = weight_type("what kind of product is this measured in weight wise "
                         "Options {Eggs , Kilos , Grams , Litres , Millilitres ")
    if all_product_weight != "eggs":
        weight_value = num_check(f"How much of your weight is in the  {name} ")
    else:
        weight_value = int_check("how many eggs are in this product")
    all_product_costs = num_check("How much does this product cost in dollars")


    all_weight = weight_value * all_product_weight
    all_unitprice = all_product_costs / all_weight
    all_unitprice.append(all_unitprice)
    all_names.append(name)
    all_product_costs.append(all_product_costs)
    all_product_weight.append(weight_value)
    all_product_weight_type.append(all_product_weight)
    productnum += 1
print(all_product_weight)
print(all_product_costs)

if budget >= min(all_product_costs):
    # Import required library
    import pandas as pd
    from tabulate import tabulate

    print("These Are Your Items")
    table_df = pd.DataFrame({
        "Name": all_names,
        "Cost ($)": all_product_costs,
        "Weight": all_product_weight,
        "Weight_Type": all_product_weight_type,
        "Price_per_kilo ($)": all_unitprice,
    })

    # Displaying the DataFrame as a formatted table using 'grid' format
    product_table = tabulate(table_df, headers='keys', tablefmt='pipe')

    print(product_table)
    # mark unaffordable stuff and adjust all accordingly if none affordable skip to step 9 -- step 6
    # Remove marked items and the others -- step 7
    # makes items in the list equal zero when they're below the budget this is, so I can remove them from
    # being used in the second step
    # changes all things over budget to 100
    for i in range(len(all_product_costs)):
        if all_product_costs[i] > budget:
            all_product_costs[i] = -100
            all_unitprice[i] = -100
            all_product_weight[i] = -100
            all_product_weight_type = -100
            all_names = -100
    condition = lambda o: o == -100  # condition cant be zero

    # Creating a copy of the list to avoid modifying it during iteration
    # removes items that are 100
    for x in all_product_costs[:]:
        if condition(x):  # if it meets the condition of being zero remove it
            all_product_costs.remove(x)
            all_unitprice.remove(x)
            all_product_weight.remove(x)
            all_product_weight_type.remove(x)
            all_names.remove(x)

    # Checks for items in unit price that aren't the minimum and makes them 100 including cost and weight
    for i in range(len(all_product_costs)):
        if all_unitprice[i] > min(all_unitprice):
            all_unitprice[i] = -100
            all_product_costs[i] = -100
            all_product_weight[i] = -100
            all_product_weight_type = -100
            all_names = -100
    # Creating a copy of the list to avoid modifying it during iteration
    # removes items that are 100
    for x in all_product_costs[:]:
        if condition(x):  # if it meets the condition of being zero remove it
            all_product_costs.remove(x)
            all_unitprice.remove(x)
            all_product_weight.remove(x)
            all_product_weight_type.remove(x)
            all_names.remove(x)



