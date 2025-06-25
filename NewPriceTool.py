import tabulate
# functions go herre
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
chipsc  =5
# weight of the chips in kilos
chipswk =.5
# weight of the chips in grams
chipswg =500
# unit price of the chips
chipsup =10

#cost of the apple
applec = 1
# weight of the apple in kilos
applewk =.25
# weight of the apple in grams
applewg =250
# unit price of the apple per kilo
appleup =4

#cost of the chocolate
chocolatec =5.25
# weight of the chocolate in kilos
chocolatewk =7.5
# weight of the chocolate in grams
chocolatewg = 7500
# unit price of the chocolate per kilo
chocolateup =0.7
chipsl = [chipswg , chipswk , chipsc , chipsup]
applel = [applewg, applewk , applec , appleup]
chocolatel = {chocolatewg , chocolatewk , chocolatec , chocolateup}

print(make_statement("Price Tool", "🍴"))
# asks if the user would like to see the instructions
print()
want_instructions = yes_no_check("do you want to see the instructions")
print()

if want_instructions == "yes":
    instructions()
    #Asks what the users budget is
budget = num_check("What is Your Budget")
# prints out the users budget in case you forgot IDK
print(f" {budget:.2f}$ is your budget")
# prints out the multiple different options and formats the weight into kg /litres
print(f"{chocolatel}")

print(tabulate(chocolatel, headers = "firstrow", tablefmt = "rst"))

