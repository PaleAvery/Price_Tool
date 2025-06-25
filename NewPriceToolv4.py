
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
print()
want_instructions = yes_no_check("do you want to see the instructions")
print()

if want_instructions == "yes":
    instructions()
    #Asks what the users budget is
budget = num_check("What is Your Budget")
# prints out the users budget in case you forgot IDK
print(f" {budget:.2f}$ is your budget")
# prints out the multiple different options and their category such as weight grams , weight kilos , cost $ , unit price $, User budget
from tabulate import tabulate
a = [['Chips',f'{chipswg:.2f}g',f'{chipswk:.2f}Kg' ,f'{chipsc:.2f}$' ,f'{chipsup:.2f}$',f'{budget:.2f}$' ], ['Apple',f'{applewg:.2f}g',f'{applewk:.2f}Kg',f'{applec:.2f}$',f'{appleup:.2f}$' ], ['Chocolate',f'{chocolatewg:.2f}g',f'{chocolatewk:.2f}Kg',f'{chocolatec:.2f}$',f'{chocolateup:.2f}$' ]] # data
b = ['Name', 'Weight Grams','Weight Kilos', 'Cost[$]', 'Unit Price per kilo','User Budget'] # headers
print("this is the available products")
print(tabulate(a, headers=b))
# filters the remaining stuff in regard to budget in two-step
# step one check if user can afford stuff off of the general cost
chip = [chipsc, chipswg,chipswk,chipsup]
apple = [applec,applewg,applewk,appleup]
choc = [chocolatec,chocolatewg,chocolatewk,chocolateup]
cost = [chipsc,applec,chocolatec]
unitprice = [chipsup, appleup , chocolateup]
# makes items in the list equal zero when they're below the budget this is, so I can remove them from
# being used in the second step
for i in range(len(cost)):
    if cost[i] > budget:
        cost[i] = 'x'
        unitprice[i] = 'x'

# prints the current values i am using this to test
print(cost)
print(unitprice)
# shows the values that are currently in budget and can afford for testing purposes
for x in range(len(cost)):
    if cost[x] != 'x':
      #  print(cost[0])
     #   print(cost[1])
    #    print(cost[2])
   #     print(unitprice[0])
  #      print(unitprice[1])
 #       print(unitprice[2])
#step two find out the lowest price per kilo and see if the user can afford it by
# comparing it to the price
    # i start by sorting the unit prices in order of lowest to highest
    # this helps weed out the best money can buy

        if unitprice[0] != 'x':
            print(unitprice[0])
        elif unitprice[1] != 'x':
            print(unitprice[1])
        elif unitprice[2] != 'x':
            print(unitprice[2])





