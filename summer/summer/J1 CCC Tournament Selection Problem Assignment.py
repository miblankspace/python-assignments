#Name: Michelle Tan
#Teacher: Ms. Brace
#Course: ICS 3O0
#Date: July 17th, 2020

#Program: Each player in a tournament plays six games. There are no ties.
#This program places the players in groups based on how many wins they have.

#Writes a function tournament that will decide which group the player is in
def tournament():

    #Counters for the number of games and the number of wins
    i = 0
    win = 0

    #Asks the user for inputs (win or loss) 6 times, adds to the win counter when w or W is inputed
    #When something other than w/W or l/L is given, the program asks for the input again until
    #a correct input is given
    while i < 6:
        record = input("\nWin or Loss (W/L): ")
        if record == "w" or record == "W":
            win = win + 1
        if record != "w" and record != "W" and record != "l" and record != "L":
            while True:
                print("\nInvalid input.")
                record = input("\nInput again (W/L): ")
                if record == "w" or record == "W":
                    win = win + 1
                    break
                elif record == "l" or record == "L":
                    break
        i = i + 1

    #If statements to place players in groups based on their number of wins
    if win >= 5:
        return "1"
    elif win == 3 or win == 4:
        return "2"
    elif win == 1 or win == 2:
        return "3"
    else:
        return "-1 (eliminated)"

#Writes a function name to ask for the player's name and converts it to title case   
def name():
    name = input("\nPlayer name: ")
    name = name.title()
    return name

#Prints a description of the program for the user
print("Please input your win/loss record for each of the games. \nYou will then be placed \
into a group depending on your record.")

#Loops the main part of the program if the user wants to run it again
while True:

    #Prints their name and the group they are in
    print("\n"+name()+", you are in group number %s"%tournament()+".\n")

    #Asks the user if they want to move on to the next player to run the
    #program again; program runs if answer starts with y or Y and
    #stops if answer starts with n or N or anything else
    answer = input("Next player? (y/n): ")
    if answer[0] == "y" or answer[0] == "Y":
        continue
    elif answer[0] == "n" or answer[0] == "N":
        break
    else:
        print("\nInvalid input.")
        break
