#check users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input("Do you want to read the instructions?").lower

        if response == "yes":
            return "yes"
        elif response == "no":
            return "no"
        else:
            print("You did not choose a valid response")


#Main routine
want_instructions = yes_no("Do you want to read the instructions?")
print(f"You chose {want_instructions}")

roll_again = yes_no("Do you want to roll again?")
print(f"if you said{roll_again}to rolling again")
