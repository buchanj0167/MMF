# functions goes here

# checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        # if response is blank outputs error
        if response == "":
            print("Put in a bloody input u idiot")
        else:
            return response


# main routine goes here
while True:
    name = not_blank("Enter your government bloodclart name (or 'xxx' to quit) ")
    if name == "xxx":
        break

print("We are done")
