def int_check(question):
    """Checks users enter an integer that is more than zero (or the 'xxx' exit code)"""

    error = "oops - please enter an integer."

    while True:

        try:
            response = int(input(question))

            return response

        except ValueError:
            print(error)

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


loop = + 1
while loop:
    budget = num_check("what is the budget")
    # show unit price regarding their sold sizes
    PacnSavCost = 5
    woolworthscost = 1
    newworldcost = 5.25
    # shows unit price per kilo
    Pacnsav = 10.00  # 10$ per kilo
    woolys = 4.00  # 4 $ per kilo
    newworld = 0.70  # 70c per kilo

    Pacnsav_weight = .5  # weighs 500g or .5kg
    wooly_weight = .25  # weighs 250g or 0.25Kg
    newworld_weight = 7.5  # weighs 7500g or 7.5Kg

    my_cost = [PacnSavCost, woolworthscost, newworldcost]
    my_numbers = [Pacnsav, woolys, newworld]
    my_weights = [Pacnsav_weight, wooly_weight, newworld_weight]

    # my_cost.sort()
    # my_numbers.sort()
    # my_weights.sort()

    # this displays what the user can afford later
    # I will isolate variables and compare price by kilo if user can afford it
    filtered_cost = list(filter(lambda x: x <= budget, my_cost))
    print(f"This is Unit Price       {filtered_cost}")
    filtered_numbers = list(filter(lambda x: x <= budget, my_numbers))
    print(f"This is Price Per Kilo   {filtered_numbers}")
    filtered_weights = list(filter(lambda x: x <= budget, my_weights))
    print(f"This is The Weight in Kg {filtered_weights}")

    # filteredovenmore = list(filter(lambda x: x <=  <= ))
    filtered_numbers.sort()
    print(filtered_numbers)
    if budget >= newworldcost:
        print("you Should buy Newworld Apples")
        key = 'Newworld'
        key2 = f" which weights {newworld_weight}Kg and costs {newworldcost}"
        cost = newworldcost
        break
    elif budget < newworldcost >= PacnSavCost and Pacnsav < woolys:
        print("you should buy PacnSav")
        key = 'PacnSav'
        key2 = f" which weights {Pacnsav_weight}Kg and costs {PacnSavCost}"
        cost = PacnSavCost
        break

    elif newworldcost > budget >= woolworthscost and Pacnsav > woolys:
        print("you should buy Woolys")
        key = 'Woolworths'
        key2 = f" which weights {wooly_weight}Kg and costs {woolworthscost}"
        cost = woolworthscost
        break
    else:
        print("you dont have enough money to buy anything")
        key = 'poor'
        break
print("tm")
if key != 'poor':
    ask = yes_no_check(f"would you like to buy {key} apples "
                   f"{key2}$")
    if ask == "yes":
        print(f"you chose to buy the {key} apple")
        print(f" you have {budget - cost}$ left")
    else:
        print(f"you didn't buy the {key} apple")
