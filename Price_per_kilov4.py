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


# apple weights 2Kg unit price 5$ unit price per kilo 5$
loop = 5
while loop:
    budget = num_check("what is the budget")
    # show unit price regarding their sold sizes
    evillebron = 5  # 500g
    woolyscost = 1  # 4kg
    newworldcost = 5.25  # 500g
    # shows unit price per kilo
    apple = 10.00
    woolys = 4.00
    newworld = 0.70


    apple_weight = .5
    wooly_weight = .25
    newworld_weight = 7.5
    print( [apple_weight, wooly_weight, newworld_weight])
    print([evillebron, woolyscost, newworldcost])
    print( [apple, woolys, newworld])

    if evillebron != 100
    # my_cost.sort()
    # my_numbers.sort()
    # my_weights.sort()
