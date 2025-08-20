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
Then the amount of items you wish to add
Then type in you items details INDIVIDUALLY 
such as 
NAME
Kind of weight unit 
WEIGHT VALUE 
PRICE 
then the code will repeat until you have done the same amount of products as you have asked for 
an if two items are recommendations you have the option to pick a recommendation or not 
PS if you type an impossibly high number just type xxx while naming something

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
        if response == "pounds" or response == "lbs" :
            return "pounds"
        if response == "ounces" or response == "oz" :
            return "ounces"
        if response == "millilitres" or response == "ml":
            return "millilitres"

        else:
            print("Please say its weight unit eg kilo , grams, litres, eggs , tons , millilitres , tons , pounds , ounces.\n")

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
# first 5 exist to store list data for recommendations

recon = []
recoc = []
recow = []
recowt = []
recoup = []


# this code stores general information for the products
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

    #--Asks what the users budget is
budget = num_check("What is Your Budget")
# setting variables for my product numbers and the kind of weight for later
productnum = 0
weight_kind = 0

#-- prints out the users budget in dollars ($)
print(f" {budget:.2f}$ is your budget")


while True:

    productmax = int_check("how many products do you want to add")
    if productmax >0:
        break
    else:
        print("please enter number higher than zero ")

# this means while my number of products is below the maximum amount of products is selected
while productnum < productmax:
    # this collects the products name
    name=not_blank("what is your products name ")
    if name == "xxx":
        break


    # this collects the unit of weight for the product
    weight = weight_type("what kind of product is this measured in weight wise "
                         "Options {Eggs , Kilos , Grams , Litres , Millilitres, tons , pounds , ounces ")

    if weight != "eggs":
        # i added a while true because a integer checker usually lets negetive num and zero pass
        # through so i added this so that the if statement can function and loop until you type a valid number
        while True:
            # I chose int checker because the unit isnt allowed to use integers
            # it also collects the amount of weight of the weight value
            weight_value = num_check(f"How much of your weight is in the  {name} ")
            if weight_value > 0:
                break
            else:
                print("please enter number higher than zero ")
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
            weight_kind = 50/1000
        elif weight == "pounds":
            weight_kind = 1/2.205
        elif weight == "ounces":
            weight_kind = 1/35.274

        else:
            weight_kind = 1000
    # this code will gather my variables and save them to lists then loop until product num == product max

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
    # adds one to the loop so it can end when it == product max
    productnum += 1




# filler line of code solely to have an event encase user is poor
if len(all_product_costs) != 0:

    # this code from lines 200 to 212 help by ensuring that the initial recommendation/s are taken and put in a temp list
    for i in range(len(all_product_costs)):
        if all_unitprice[i] == min(all_unitprice):
            recon.append(all_names[i])
            recoc.append(all_product_costs[i])
            recow.append(all_product_weight[i])
            recowt.append(all_product_weight_type[i])
            recoup.append(all_unitprice[i])

            # Import required library
            import pandas as pd
            from tabulate import tabulate

            print("This is the initial list of stuff you can afford ")
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
    #clearing the lists as i plan on using them later for something
    all_product_weight.clear()
    all_product_costs.clear()
    all_names.clear()
    all_product_weight_type.clear()
    all_unitprice.clear()
    # Import required library



    # Import required library
    import pandas as pd
    from tabulate import tabulate
    # this displays the initial recommendations
    # using tabulate to make it look nice
    print("This is the recommendation/s")
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
    # this detects whether the system has duplicates for recommendations
    if len(recoup) != len(set(recoup)):
        option = yes_no_check("Seems like you have multiple Recommendations would you like to pick one ")
        if option == "yes":
            while True:
                picker = int_check(
                    f"which one would you like to pick as your primary recommendation pick from 0 - {len(recoc) -1}")
                # this code helps determine a range of values the code can accept e.g. 0-2 e.g. 0-3
                if len(recoc) -1 >= picker > -1:
                    # this code takes the value of the picker and appends to the blank lists the value of picker to the empty lists
                    all_names.append(recon[picker])
                    all_product_weight_type.append(recowt[picker])
                    all_unitprice.append(recoup[picker])
                    all_product_weight.append(recow[picker])
                    all_product_costs.append(recoc[picker])
                    # this displays the initial recommendations
                    print("This is the final recommendation")
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
                    break
                #if your code isn't within the range it loops
                else:
                    print(f"you typed a number above or below the range of 0 - {len(recoc) -1}")

        else:
            print("These are what i recommend then ")
            print(product_table)







# if the list is empty / you cant afford anything this shows up
else:
    print("i cant recommend anything  as you cant afford any of it")
