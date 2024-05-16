# ENSF 692 Spring 2024
# May 14 Lab 3
# Input With Functions

# Add comments to explain the functionality of this program


def get_user_input(n):
    entry = input("Please type any entry #" + str(n + 1) + ": ")
    return entry, type(entry)

def process_user_input(n, entry, type):
    print("This is entry #" + str(n + 1) + ":", entry)
    print("The type of entry #" + str(n + 1) + " is :", str(type))


# Input Method 3
print('\n' * 2)
print("***METHOD 3***")
num_of_repeats = 3 #Number of inputs the user will be asked for
results = [] #Stores the user inputs
results_types = [] #Stores the type of vars of the user input

# Iterate for each user input 
for i in range(num_of_repeats):
    # Call a function that gets user input and returns the input and input tupe
    a, b = get_user_input(i)
    # Populate the results list with the user input
    results.append(a)
    # Populate the result types list with the user input
    results_types.append(b)

# Iterate for each user input 
for i in range(num_of_repeats):
    # Print the results for each stored input
    process_user_input(i,results[i], results_types[i])

