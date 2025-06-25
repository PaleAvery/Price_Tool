
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


def Kg_g_check(question):
    """Checks that users enter yes / y or no/n to a question"""
    #

    while True:
        response = input(question).lower()

        if response == "kilo" or response == "kg":
            return "Kg's"
        if response == "Grams" or response == "g":
            return "G's"
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



limit = num_check("how much is your budget")
print(f"your budget is ${limit:.2f}")
unit = Kg_g_check("would you like to use kilos or grams")
print(f"you picked {unit}'s")

item = not_blank("what is your items name")
print(f"your item is {item}")
weight = num_check("how much does your item weigh")
print(f"your {item} weighs {weight} {unit} ")
price = num_check("how much does your item cost")
print(f" {item} costs {price:.2f} ")

if limit <= price:
    print("price is above budget")
else:
    keep_on = yes_no_check("would you like to add another item")
