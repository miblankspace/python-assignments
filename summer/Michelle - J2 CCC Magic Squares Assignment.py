#Name: Michelle T
#Teacher: Ms. Brace
#Course: ICS 3O0
#Date: July 20th, 2020

#Program: Writes a program that asks a user for a 4 x 4 square of numbers 
#and returns whether or not it is a magic square.

#Writes a function magic that determines if something is a magic square or not
def magic():

    #Identifies variable that stores all 16 integers
    list_of_lists = []

    #Adds inputs to list_of_lists by splitting them into a list,
    #converting them into integers using temporary variables
    #numbers and strings, and adding them to list_of_lists
    for i in range(4):
        numbers = [0,0,0,0]
        line = input("\nPlease input 4 integers, each separated by a space: ")
        strings = line.split()
        for i in range(len(strings)):
            numbers[i] = int(strings[i])
        list_of_lists.append(numbers)

    #New variables to store the total value to be compared to,
    #and the list that will contain the column values
    total = sum(list_of_lists[0])
    new_list_of_lists = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    #Converts list of rows to list of columns
    #Checks conditions if it is not a magic square
    for i in range(4):
        row = list_of_lists[i]
        for j in range(4):
            value = row[j]
            new_list_of_lists[i][j]=list_of_lists[j][i]
        column = new_list_of_lists[i]
        if sum(row) != total or sum(column) != total:
            return "\nNot magic"                
    return "\nMagic"

#Prints an explanation of the program
print("This program asks for a 4 x 4 square of numbers \
and tells you \nwhether or not those numbers make a magic square.")

#Loops the program if the user wants to run it again (decided using input)
while True:
    print(magic())
    answer = input("\nRun again? (y/n): ")
    if answer[0] == "y" or answer[0] == "Y":
        continue
    elif answer[0] == "n" or answer[0] == "N":
        print("\nGoodbye!")
        break
    else:
        print("\nInvalid input.")
        break

