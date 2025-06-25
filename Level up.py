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


def action(question):
    """Checks that users enter yes / y or no/n to a question"""
    #

    while True:
        response = input(question).lower()

        if response == "punch" or response == "p":
            return "punch"
        if response == "heal" or response == "h":
            return "heal"
        else:
            print("please enter punch or heal.\n")


loop = + 1
while loop:
    budget = num_check("what is the budget")
    # show unit price regarding their sold sizes

    my_level = 1

    # my_cost.sort()
    # my_numbers.sort()
    # my_weights.sort()

    # this displays what the user can afford later
    # I will isolate variables and compare price by kilo if user can afford it
