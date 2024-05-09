# ENSF 592 Spring 2023
# May 9 Lab 2
# Exercise 2 - Solutions

# Add comments to explain the functionality of this program

# Input Method 1
# Formatting the user prompt output
print('\n')
print("***METHOD 1***")
# Requesting an input from the user
input1 = input("Please enter your name: ")
# Print user input
print("This is the first input:", input1)


# Input Method 2

# Formatting the user prompt output
print('\n' * 2)
print("***METHOD 2***")
# Sanitizing the input data to be "x" and nothing else
while True:
    #Requesting an input from the user
    input2 = input("I am looking for specific input. You must type x: ")
    if input2 == "x":
        break
#Print user input
print("This is the second input: " + input2)


# Rewrite Input Method 2 so that no break statement is necessary 

# Formatting the user prompt output
print('\n' * 2)
print("***METHOD 2++***")

inputIsx = True
# Sanitizing the input data to be "x" and nothing else
while inputIsx:
    #Requesting an input from the user
    input2 = input("I am looking for specific input. You must type x: ")
    #Check if input is "x"
    if input2 == "x":
        #Exit out of sanitization loop
        inputIsx = False
#Print user input
print("This is the second input: " + input2)