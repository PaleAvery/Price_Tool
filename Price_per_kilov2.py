import tabulate
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
loop = 5
while loop:
    budget = num_check("what is the budget")
    # shows unit price per kilo
    apple = 5
    woolys = 2.5
    newworld = 6
    # show unit price regarding their sold sizes
    applecost = 2.5
    woolyscost = 10 #per kilo 10$
    newworldcost = 3 #3$ per kilo

    apple_weight = applecost / apple
    wooly_weight = woolyscost / woolyscost
    newworld_weight = newworldcost / newworld
    # a list of numbers
    my_cost = [applecost, woolyscost, newworldcost]
    my_weight = [apple_weight, wooly_weight, newworld_weight]
    my_numbers = [apple, woolys, newworld]

    if any(y > budget for y in my_numbers):
        print(my_numbers)





