# calgary_dogs.py
# Jaskirat Singh (Jazz)
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import pandas as pd

def main():
    # Import data here
    dog_breeds_data = pd.read_excel("CalgaryDogBreeds.xlsx")
    dog_breeds_data.set_index(['Breed', 'Year', 'Month'], inplace=True)
    print("ENSF 692 Dogs of Calgary")

    # User input stage and convert to all uppercase to make it case-insensitive

    while True:
        # Get user input for dog breed and convert to uppercase
        dog_breed_input = input("Please enter a dog breed: ").upper()
        try:
            if dog_breed_input in dog_breeds_data.index.get_level_values('Breed').str.upper():
                break
            else: raise KeyError
        except KeyError:
            print("Dog breed not found in the data. Please try again.")

    # Data anaylsis stage

    ## 1. Find and print all years where the selected breed was listed in the top breeds.
    # Create filter for breed matched with user input
    breed_filter = dog_breeds_data.index.get_level_values('Breed').str.upper() == dog_breed_input
    dog_breed_data = dog_breeds_data[breed_filter]
    
    # Get list of unique years of data entries (no need to sort as data is pre-sorted)
    years_listed = dog_breed_data.index.get_level_values('Year').unique()
    # Print message for project requirement
    print(f"The {dog_breed_input} was found in the top breeds for years: {' '.join(map(str, years_listed))}")

    ## 2. Calculate and print the total number of registrations of the selected breed found in the dataset.
    # Total registrations for chosen breed
    total_registrations = dog_breed_data["Total"].sum()
    print(f"There have been {total_registrations} {dog_breed_input} dogs registered total.")

    ## 3. Calculate and print the percentage of selected breed registrations out of the total percentage for each year (2021, 2022, 2023).
    # Total registrations for chosen breed for each year
    breed_registrations = dog_breed_data.groupby(level='Year')['Total'].sum()

    # Index-slicing setup according to pandas documentation
    idx = pd.IndexSlice

    # Total registrations for all breeds for each year
    all_breeds_registrations = dog_breeds_data.loc[idx[:, 2021:2023, :], :].groupby(level='Year')['Total'].sum()

    # Percentage of selected breed registrations out of the total for each year
    breed_percentages = breed_registrations / all_breeds_registrations * 100

    # Print the percentages
    for year, percentage in breed_percentages.items():
        print(f"The {dog_breed_input} was {percentage:.6f}% of top breeds in {year}.")

    ## 4. Calculate and print the percentage of selected breed registrations out of the total three-year percentage.
    # Total registrations for all the years for chosen breed
    breed_total_three_years = breed_registrations.sum()

    # Total registrations for all the years for all breeds
    total_three_years = all_breeds_registrations.sum()

    # Percentage of selected breed registrations out of the total for all years
    total_breed_percentages = breed_total_three_years / total_three_years * 100

    # Print the total percentage
    print(f"The {dog_breed_input} was {total_breed_percentages:.6f}% of top breeds across all years.")

    ## 5. Find and print the months that were most popular for the selected breed registrations. Print all months that tie.
    # Find the months that were most popular for the selected breed registrations
    month_counts = dog_breed_data.index.get_level_values('Month').value_counts()

    # Match number of month count to the max month counts
    most_popular_months = month_counts[month_counts == month_counts.max()].index.tolist()

    # Sort output alphabetically to match screenshot
    most_popular_months.sort()

    # Print the most popular months
    print(f"Most popular month(s) for {dog_breed_input} dogs: {' '.join(most_popular_months)}")


if __name__ == '__main__':
    main()
