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

        print("Sorry, this cant be blank. Please try again.\n")


nameofproduct = []
price_per_wt = []
weight_kilo = []
weight_gram = []
# main routine goes here

# loop for testing purposes
while True:
    # asks for the name of product
    nameofproduct = not_blank("what is the product")
    # asks for what unit of measurement to use
    Weight = Kg_g_check("would you like to use Grams or Kilos")
    # if the user  chooses kilos ask for weight in kilos
    if Weight == "Kilo":
        weight_kilo = num_check("how much does your thing weigh in kgs")
        # ask for price for kilos
        price_per_wt = num_check("how much does this cost per kg")
    # if the user picks Grams ask for weight in grams
    elif Weight == "Grams":
        weight_gram = num_check("how much does your thing weigh in grams")
        # ask for price per gram
        price_per_wt = num_check("how much does this cost per g")
        # pint out how much kilos the user picked how much it is worth total
    if Weight == "Kilo":
        print(
            f"your {nameofproduct} is {weight_kilo:.2f} Kilos which is {weight_kilo * 1000:.2f} Grams which costs ${price_per_wt * weight_kilo:.2f} ")
    elif Weight == "Grams":
        print(
            f"your {nameofproduct} is {weight_gram:.2f} Grams which is {weight_gram / 1000:.2f} Kilos which costs ${price_per_wt * weight_gram:.2f} ")
