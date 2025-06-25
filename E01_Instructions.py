# Functions go here
def make_statement(statement, decoration):
    """ Emphasises headings by adding decoration
     at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """Checks the users enter the full word
    or the 'n' letter/s of a worf from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"please choose an option from {valid_answers}")


def instructions():
    make_statement("Instructions", "?")

    print('''

TBC.

    ''')


# Main routine goes here

make_statement("Price_Tool", "🔧")

print()
want_instructions = string_check("do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()
print("Program continues")
