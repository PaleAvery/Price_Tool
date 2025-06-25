
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


limit = num_check("how much is your budget")
print(f"your budget is ${limit:.2f}")

number = num_check("keep under budget")
if limit <= number:
    print("number is above budget")
else:
    number = num_check("keep under budget")