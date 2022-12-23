#Name: Michelle T
#Teacher: Ms. Brace
#Course: ICS 3U0
#Date: July 24th, 2020

#Program: Given some text and a string, this program determines if the text
#contains a cyclic shift of the string.

#Writes a function cyclic that determines if the text contains a cyclic shift of the string
def cyclic():

    #Identify variables t for the inputed text and s for the inputed string
    t = input("\nPlease input some text in uppercase: ")
    s = input("\nPlease input some string in uppercase: ")

    #Checks if either the text or the string is not in uppercase, returns an error message
    if not t.isupper() or not s.isupper():
        return("\nError. Make sure both your text and the string are in uppercase.")

    #Identify new variable shiftlist to hold the shifted strings
    shiftlist = []

    #Adds shifted strings to shiftlist by slicing
    for i in range(len(s)):
        first = s[i:]
        second = s[:i]
        shiftlist.append(first + second)

    #Checks if any shifted string which is held in shiftlist is in the text
    #Returns yes if there is, no if there is not
    for j in shiftlist:
        if j in t:
            return "\nyes"
    return "\nno"
    
#Describes the program for the user
print("Given some text and a string, this program determines\nif the text contains \
a cyclic shift of the string.")

#Loops this part of the program while true
while True:

    #Calls and prints the returned value of cyclic
    print(cyclic())

    #Asks if user wants to run the program again
    #If the inputed answer is 'y' or 'Y', the program will run again
    #Otherwise, it will print 'Goodbye!' and stop
    answer = input("\nRun again? Type \"y\" to continue: ")
    if answer == "y" or answer == "Y":
        continue
    else:
        print("\nGoodbye!")
        break
