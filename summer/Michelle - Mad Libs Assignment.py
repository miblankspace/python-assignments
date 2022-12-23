#Name: Michelle
#Teacher: Ms. Brace
#Course: ICS 3O0
#Date: July 12th, 2020

#Program: writes a Mad Libs story

#Prints instructions for the player
print("WELCOME TO THE MAD LIBS PROGRAM!\n\n\
In this program, you will be asked to input a few words.\n\
A story will be made based on the words you inputed.\n\
Once you have finished typing a word, press ENTER to continue to the next line.\n")

#Asks the player to input their name and writes an introductory message
name = input("To start, please type your name: ")

print("\nHello, "+ name[0].upper() + name[1:].lower() + "! Let's get started.\n")

#Loops the program if the player wants to play again
while True:

    #Stores the inputed verbs as variables, changes capitalization if needed  
    a = input("Please input an adjective: ").lower()
    b = input("Please input a verb (present continuous tense, ending in \"ing\"): ").lower()
    c = input("Please input an adverb: ").lower()
    d = input("Please input a noun (object): ").lower()
    e = input("Please input a funny-sounding word: ").upper()

    #Prints the story using inputed words stored in variables above
    print("\nThank you! Here is your custom Mad Libs story!\n\n\
I woke up today feeling " + a + " because I had a big " + b + " competition.\n\
I packed my things and ran " + c + " out the door.\nI was already at the venue \
when I realized that I forgot to take my " + d + "\nthat was absolutely essential \
to the " + b + " competition with me! " + e + "!\n\nThank you for playing Mad Libs.")

    #Loops the question "Play again" until a valid answer (y/n) is given
    while True:
        answer = input("\nPlay again? (y/n): ")
        if answer in("y", "n"):
            break
        else:
            print("\nInvalid input.")
            continue

    #Restarts from part of the program if "y" is typed to play again, otherwise break and exits program    
    if answer == "y":
        print("\nBack again aren't you, " + name[0].upper() + name[1:].lower() + "?\n")
        continue
    else:
        print("\nGoodbye!")
        break




