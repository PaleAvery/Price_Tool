def make_statement(statement, decoration):
    """ Emphasises headings by adding decoration
     at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"




def food_list(question):
    """Checks that a user response is not blank """

    while True:
        response = input(question)

        if response != "":
            return response


def instructions():
    print(make_statement("instructions", "*"))

    print('''


    Shows Instructions

        ''')


def yes_no(question):
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


def budget(question, num_type="float"):
    """checks response is a float integer or more than zero"""
    if num_type == "float":
        error = "please enter a number more than zero."
    else:
        error = "please enter an integer more than zero."

    while True:
        try:

            if num_type == "float":
                response = int(input(question))
            else:
                response = int(input(question))

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


print(make_statement("fund raising calculator", "7"))

print()
want_instructions = yes_no("do you want to see the instructions")
print()

if want_instructions == "yes":
    instructions()

print()

limit = food_list('what is your food item')
str['apple'] = '20'
banana = '10'

print(f"you have picked the {limit} which is worth {float(limit):.2f}$")
