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

apple['fresh_fruit','tree apple','newworld','woolys' ]
Fresh_Fruit_Apples_Royal_Gala_fromwoolys = 4.95
apple_from_random_tree = 0
Royal_Gala_Apples_fromnewworld = 5.99

budget = num_check("what is your budget")
print(f"{Fresh_Fruit_Apples_Royal_Gala_fromwoolys:.2f}$ and {apple_from_random_tree:.2f}$ and {Royal_Gala_Apples_fromnewworld:.2f}$")
if Fresh_Fruit_Apples_Royal_Gala_fromwoolys < budget:
    print(Fresh_Fruit_Apples_Royal_Gala_fromwoolys)
if apple_from_random_tree < budget:
    print(apple_from_random_tree)
if Royal_Gala_Apples_fromnewworld < budget:
    print(Royal_Gala_Apples_fromnewworld)

if apple_from_random_tree < Royal_Gala_Apples_fromnewworld and Fresh_Fruit_Apples_Royal_Gala_fromwoolys:
    print("apple is the right choice")