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

#writes a function convert_string that consumes a string and produces the number of
#uppercase, lowercase, and other characters and also converts it to title case
def convert_string(something):

    #local variables that serve as counters for each type of character
    uppercase = 0
    lowercase = 0
    other = 0

    #writes a for loop - i check every letter in the inputed word
    #for loop runs as long as i is still within the letters (length) of the word
    for i in something:

        #checks if the letters are lowercase, uppercase, or other (except for whitespace)
        #if the letters are in the lowercase/uppercase libraries, the counter adds 1
        if i in alphabet_lower:
            lowercase = lowercase + 1
        elif i in alphabet_upper:
            uppercase = uppercase + 1
        elif i != " ":
            other = other + 1

    #converts the string to title case
    title_case = something.title()

    #returns the new values of the counters as well as the string in title case
    return "\nThe number of lowercase letters in your string is %s"%lowercase +".\n\
The number of uppercase letters in your string is %s"%uppercase + ".\n\
The number of other characters (excluding whitespace) in your string is %s"%other + ".\n\n\
Here is your string in title case: %s"%title_case

#prints a hello message and explains what theh program is about
print("Hello! This program will return the number of uppercase\
, lowercase, \nand other characters. It will also return your string in title case.")

#loops the program
while True:

    #asks the user to input a string
    string = input("\nPlease input a string: ")

    #prints the function convert_string consuming the variable string
    #the variable string uses the string that the user inputed
    print (convert_string(string))

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
        
    
