#Name: Michelle T
#Teacher: Ms. Brace
#Course: ICS 3U0
#Date: July 23rd, 2020

#Program: Creates a program that asks the user for an input, reads the input,
#and follows one of seven instructions based on the input

#Writes a function punchy that follows one of seven instructions based on the input
def punchy():

    #Initial values of a and b
    a = 0
    b = 0

    #Loops the program 
    while True:

        #Asks user for instruction input
        inputs = input("\nPlease input your instructions: ")

        #Sets instruction to the first value, which determines what instruction number to follow
        instruction = inputs[0]
        
        #Checks if instruction is not a digit
        if not instruction.isdigit():
            print("\nNot a valid instruction.")
            return again()

        #Converts instruction to int
        instruction = int(inputs[0])

        #Checks if instruction value not in range
        if instruction < 0 or instruction > 7:
            print("\nNot a valid instruction.")
            return again()

        #Sets variables to the values of either a or b, or sets n to variable 2 if it is a digit
        #var1 and var2 are temporary variables used to follow the instructions
        #If it is not A, B, or a digit in variable 2, print invalid input
        if len(inputs) > 1:
            var1 = inputs[1]
            if var1 == "A":
                var1 = a
            elif var1 == "B":
                var1 = b
            else:
                print("\nInvalid input.")
                return again()
            if len(inputs) > 2:
                var2 = inputs[2]
                if var2.isdigit():
                    n = int(var2)
                elif var2 == "A":
                    var2 = a
                    if instruction == 1:
                        n = var2
                elif var2 == "B":
                    var2 = b
                    if instruction == 1:
                        n = var2
                else:
                    print("\nInvalid input.")
                    return again()

        #The list of instructions and the changes that can take place based on instruction number
        #If instruction is equal to 7, the loop stops
        if instruction == 1:
            var1 = n
        elif instruction == 2:
            print("\nThe value of your variable is %s."%var1)
        elif instruction == 3:
            var1 = var1 + var2
        elif instruction == 4:
            var1 = var1 * var2
        elif instruction == 5:
            var1 = var1 - var2
        elif instruction == 6:
            var1 = var1 // var2
        elif instruction == 7:
            break

        #Sets either a or b to their new values, saves var1 and var2 values in a and b for next loop
        if len(inputs) > 1:
            var3 = inputs[1]
            if var3 == "A":
                a = var1
            elif var3 == "B":
                b = var1

    #Returns the function again once the loop stops
    return again()

#Writes a function again that asks if the user wants to run the program again
def again():

    #If the inputed answer is y or Y, the function punchy runs again; otherwise the program stops
    answer = input("\nDo you want to run again? Type \"y\" to continue: ")
    if answer == "y" or answer == "Y":
        punchy()
    return "\nGoodbye!"

#Program description for the user                                
print("This program reads your input instructions and produces the output.\n\n\
An instruction is an integer in the range 1...7, possibly followed by a variable\nname, \
which in turn is possibly followed by either a number or a variable.\n\
In all instructions below, the variable X or Y may refer to either A or B.\n\n\
Here are a list of instructions.\n\n1 X n means set the variable X to the integer value n\n\
2 X means output the value of variable X to the screen\n\
3 X Y means calculate X + Y and store the value in variable X\n\
4 X Y means calculate X ∗ Y and store the value in variable X\n\
5 X Y means calculate X − Y and store the value in variable X\n\
6 X Y means calculate the quotient of X/Y and store \nthe value in variable X as an integer\n\
7 means stop execution of this program")

#Calls the function punchy
print(punchy())
