# ENSF 692 Spring 2024
# May 14 Lab 3
# Review of else statement in loops

L = []  # Create a new list
nmax = 30 # Maximum number we're going up to is 30

# Iterate from 2 up to 30
for n in range(2, nmax):    # 2 to 30

    # Iterate over each value in the current form of the list L
    for factor in L:    # Variable factor holds the current value being tested in the inner loop
        # If the following is true, break the loop!
        if n % factor == 0:
            print("Loop broke early")
            break
        print("Loop finished naturally") # Loop didn't break

    # Only execute this code IF the nested loop DIDN'T break (finished naturally without encountering a break)
    else: # No break occured above (which means we should have seen Line 18 execute other than the first iteration)
        print("RUN!")
        L.append(n)  # Add the current value of n to L if the inner loop finished all iterations without breaking


print(L)  # Happens when all else is done!
