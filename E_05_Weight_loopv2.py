def Kg_g_check(question):
    """Checks that users enter yes / y or no/n to a question"""
    #

    while True:
        response = input(question).lower()

        if response == "kilo" or response == "kg":
            return "Kilo"
        if response == "Grams" or response == "g":
            return "Grams"
        else:
            print("please enter Kilo(Kg) or Gram(g).\n")


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


def not_blank(question):
    """Checks that a user response is not blank """

    while True:
        response = input(question)

        if response != "":
            return response






