# Functions

def main():
    #problem1()
    problem2()


# Create a function that has a loop
# Prompt for numbers until the user enters q to quit
# If the user doesn't enter q, ask them to input another number
# When the user enters q to quit, print the SUM of all numbers entered

def problem1():
    userInput="10"
    otherInput="10"
    #total=int(userInput +otherInput)

    while userInput!="q" and otherInput !='q':
        userInput=input("enter a letter.")
        otherInput=input("enter a letter.")

        if userInput == 'q' and otherInput =='q':
            return (userInput and otherInput)
        else:
            print("WRONG ENTRY!!!")

# Create a function
# in this function prompt the user for 2 numbers
#Create a second function called ```do_the_math``` that accepts 2 parameter
# In the ```do_the_math``` calculate the SUM, DIFFERENCE, PRODUCT, and QUOTIENT (division result)
# and return them as a dictionary to the calling function
def problem2():
    userInput="Enter a number."
    otherInput="Enter the second number."

def do_the_math():
    dict['sum': 20,'diff':2,'product':4,'quotient':5]

















    if __name__ == '__main__':
        main()