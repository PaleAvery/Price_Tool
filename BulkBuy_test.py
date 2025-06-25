cost = 0
key = 0
count = 0
budget = 0
key2 = 0

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
    bulk = yes_no_check("would you like to purchase bulk")
    if bulk == 'yes':
        count = int_check("How much would you like to buy")
    else:
        count = 1
    budget = num_check("what is the budget")
    # show unit price regarding their sold sizes
    A_Cost = 5 * count
    B_Cost = 1 * count
    C_Cost = 5.25 * count
    # shows unit price per kilo
    A = 10.00   # 10$ per kilo
    B = 4.00   # 4 $ per kilo
    C = 0.70   # 70c per kilo

    A_Weight = .5 * count  # weighs 500g or .5kg
    B_Weight = .25 * count  # weighs 250g or 0.25Kg
    C_Weight = 7.5 * count  # weighs 7500g or 7.5Kg

    my_cost = [A_Cost, B_Cost, C_Cost]
    my_numbers = [A, B, C]
    my_weights = [A_Weight, B_Weight, C_Weight]

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
    # this helps display what is the best to buy for the users price point
    # filteredovenmore = list(filter(lambda x: x <=  <= ))
    filtered_numbers.sort()
    print(filtered_numbers)
    if budget >= C_Cost:
        print("you Should buy Newworld Apples")
        key = 'C'
        key2 = f" which weights {C_Weight:.2f}Kg and costs {C_Cost:.2f}"
        cost = C_Cost
        break
    elif budget < C_Cost >= A_Cost and A < B:
        print("you should buy PacnSav")
        key = A
        key2 = f" which weights {A_Weight:.2f}Kg and costs {A_Cost:.2f}"
        cost = A_Cost
        break

    elif C_Cost > budget >= B_Cost and A > B:
        print("you should buy Woolys")
        key = 'B'
        key2 = f" which weights {B_Weight:.2f}Kg and costs {B_Cost:.2f}"
        cost = B_Cost
        break

    else:
        if count > 1 :
            print("Maybe buy a little less and not use bulk buy next time. ")
            Tryagain = yes_no_check("would you like restart your shopping")
            if Tryagain != 'yes':
                break
            key = 'poor'
        else:
            print("you dont have enough money to buy anything")
            Tryagain = yes_no_check("would you like restart your shopping")
            if Tryagain != 'yes':
                break
            key = 'poor'

final_money = budget - cost

print("tm")
if budget >= 1:
    ask = yes_no_check(f"would you like to buy {count} {key} apples "
                       f"{key2}$")
    if ask == "yes":
        print(f"you chose to buy the {key} apple")
        print(f" you have {final_money:.2f}$ left")
    else:
        print(f"you didn't buy the {key} apple")

