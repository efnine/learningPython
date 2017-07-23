def clinic():
    print ("You've just entered the clinic!")
    print ("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.\n").lower()
    print ('\n')
    if answer == "left" or answer == "l":
        print ("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right" or answer == "r":
        print ("Of course this is the Argument Room, I've told you that already!")
    else:
        print ("\nYou didn't pick left or right! Try again.")
        clinic()

clinic()