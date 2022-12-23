#name: Michelle T
#teacher: Ms. Brace
#course: ICS 3O0
#date: July 15th, 2020

#program: Receives a string and writes a function that returns the number of
#uppercase, lowercase, and other characters. Also returns the string
#in title case.

#import the library string
import string

#access the string of lowercase letters (a to z) and the string of uppercase letters (A to Z)
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

#writes a function lowercase that consumes a string and produces the number of lowercase letters
def lowercase(something):

    #local variable lowercase that serves as the counter for lowercase letters
    lowercase = 0

    #for loop to check the letters in the string as long as i is within the string letters
    for i in something:

        #if i is in the library of lowercase letters, the counter will add 1
        if i in alphabet_lower:
            lowercase = lowercase + 1

    #returns the new value of the counter
    return lowercase

#writes a function uppercase that consumes a string and produces the number of uppercase letters
def uppercase(something):

    #local variable uppercase that serves as the counter for uppercase letters
    uppercase = 0

    #for loop to check the letters in the string as long as i is within the string letters
    for i in something:

        #if i is in the library of uppercase letters, the counter will add 1
        if i in alphabet_upper:
            uppercase = uppercase + 1

    #returns the new value of the counter
    return uppercase

#writes a function other_characters that consumes a string and produces the number of other characters
def other_characters(something):

    #local variable other that serves as the counter for other characters
    other = 0

    #for loop to check the letters in the string as long as i is within the string letters
    for i in something:

        #if i is not in the library of lowercase or uppercase letters and is not whitespace, the counter will add 1
        if i not in alphabet_lower and i not in alphabet_upper and i != " ":
            other = other + 1

    #returns the new value of the counter
    return other

#writes a function that consumes a string and produces the string in title case
def title_case(something):
    title_case = something.title()
    return title_case
    
#prints a hello message and explains what theh program is about
print("Hello! This program will return the number of uppercase\
, lowercase, \nand other characters. It will also return your string in title case.")

#loops the program
while True:

    #asks the user to input a string
    string = input("\nPlease input a string: ")

    #prints the new values of the counters as well as the string in title case using the functions
    print ("\nThe number of lowercase letters in your string is %s"%lowercase(string) +".\n\
The number of uppercase letters in your string is %s"%uppercase(string) + ".\n\
The number of other characters (excluding whitespace) in your string is %s"%other_characters(string) + ".\n\n\
Here is your string in title case: %s"%title_case(string))

    #asks the user if they want to play again
    answer = input("\nWould you like to run this program again? Answer: ")

    #if the inputed answer begins with y or Y, the program will loop again
    #if the inputed answer begins with n or N, the program will print a goodbye message and stop
    #any other answer and the program will print an invalid inpnut message, a goodbye message, and stop
    if answer[0] == "y" or answer[0] == "Y":
        continue
    elif answer[0] == "n" or answer[0] == "N":
        print("\nGoodbye!")
        break
    else:
        print("\nInvalid input. Goodbye!")
        break
