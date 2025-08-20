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
# this is weight type im using this as first to find what unit of measurement it is
# and secondly on how much I alter the weight value that is given
# which is why I have it return as floats instead of words
def weight_type(question):
    """Checks that users enter yes / y or no/n to a question"""
    #

    while True:
        response = input(question).lower()

        if response == "kilo" or response == "k":
            return "kilo"
        if response == "grams" or response == "g":
            return "grams"
        if response == "litres" or response == "l":
            return "litres"
        if response == "eggs" or response == "e" or response == "egg":
            return "eggs"
        if response == "tons" or response == "t" :
            return "tons"
        if response == "millilitres" or response == "ml":
            return "millilitres"

        else:
            print("Please say its weight unit eg kilo , grams, litres, eggs , tons , millilitres.\n")

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
# this is my not blank im using this in order to Get names from my user
def not_blank(question):
    """Checks that a user response is not blank """

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this cant be blank. Please try again.\n")
# lists to hold ticket details
recon = []
recoc = []
recow = []
recowt = []
recoup = []
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
weight_kind = 0
#-- prints out the users budget in dollars ($)
print(f" {budget:.2f}$ is your budget")

productmax = int_check("how many products do you want to add")
while productnum < productmax:
    # this collects the products name
    name=not_blank("what is your products name ")
    # this collects the unit of weight for the product
    weight = weight_type("what kind of product is this measured in weight wise "
                         "Options {Eggs , Kilos , Grams , Litres , Millilitres ")

    if weight != "eggs":
        # I chose num checker because the units are allowed to have decimals
        # it also collects the amount of weight of the weight value
        weight_value = num_check(f"How much of your weight is in the  {name} ")
    else:
        # I had realized initially that I could type like half an egg, and it would be fine so
        # I wrote this block as an int checker as you cant have half an egg at the store
        weight_value = int_check("how many eggs are in this product")
    costs = num_check("How much does this product cost in dollars")
    if costs <= budget:
        # this segment adds to all my lists im using their order of the list to  determine how its displayed graph wise
        # this pushes out an absolute weight as I had calculated
        if weight == "kilo":
            weight_kind = 1
        elif weight == "grams":
            weight_kind = 1/1000
        elif weight == "litres":
            weight_kind = 1
        elif weight == "millilitres":
            weight_kind = 1/1000
        elif weight == "eggs":
            weight_kind = 56/1000
        else:
            weight_kind = 1000
        # a conversion rate of all of these and have them as relative units in terms of kilograms
        all_weight = weight_value * weight_kind
        # this calculates the price per kilo by dividing the price by the weight in kilos { price / kilo }
        unitprice = costs / all_weight
        # this adds the information on unit price to the list
        all_unitprice.append(unitprice)
        # this adds the name the user typed to the all names list
        all_names.append(name)
        # this adds the cost of your product to the all product costs list
        all_product_costs.append(costs)
        # this adds the value of the weight in numbers to the all product weight list
        all_product_weight.append(weight_value)
        # this adds the product weight type to the list
        all_product_weight_type.append(weight)

    productnum += 1

if len(all_product_costs) != 0:
    print(all_product_weight)
    print(all_product_costs)
    print(all_names)
    print(all_product_weight_type)
    print(all_unitprice)
    for i in range(len(all_product_costs)):
        if all_unitprice[i] == min(all_unitprice):
            recon.append(all_names[i])
            recoc.append(all_product_costs[i])
            recow.append(all_product_weight[i])
            recowt.append(all_product_weight_type[i])
            recoup.append(all_unitprice[i])




    # Import required library

    from tabulate import tabulate

    # Import the tabulate module
    from tabulate import tabulate

    if budget >= min(all_product_costs):
        # Import required library
        import pandas as pd
        from tabulate import tabulate

        print("These Are Your Items")
        table_df = pd.DataFrame({
            "Name": recon,
            "Cost ($)": recoc,
            "Weight": recow,
            "Weight_Type": recowt,
            "Price_per_kilo ($)": recoup,
        })

        # Displaying the DataFrame as a formatted table using 'grid' format
        product_table = tabulate(table_df, headers='keys', tablefmt='pipe')
        print(product_table)

    # this code filters out what you cant afford step one of my filtering plan
else:
    print("i cant recommend anything  as you cant afford any of it")
