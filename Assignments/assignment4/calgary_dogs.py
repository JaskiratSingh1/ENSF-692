# calgary_dogs.py
# Jaskirat Singh
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import pandas as pd
import os

def main():
    # Import data here
    dog_breeds_data = pd.read_excel("CalgaryDogBreeds.xlsx")

    print("ENSF 692 Dogs of Calgary")

    # User input stage and convert to all uppercase to make it case-insensitive

    while True:
        dog_breed_input = input("Please enter a dog breed: ").upper()
        try:
            if dog_breed_input in dog_breeds_data["Breed"].values:
                break
            else: raise KeyError
        except KeyError:
            print("Dog breed not found in the data. Please try again.")

    # Data anaylsis stage
    # Get rows with input breed as the breed
    dog_breed_data = dog_breeds_data[dog_breeds_data["Breed"].str.upper() == dog_breed_input]
    # Get list of unique years of data entries (no need to sort as data is pre-sorted)
    years_listed = dog_breed_data["Year"].unique()

    # Print message for project requirement
    print(f"The {dog_breed_input} was found in the top breeds for years: {' '.join(map(str, years_listed))}")

    




if __name__ == '__main__':
    main()
